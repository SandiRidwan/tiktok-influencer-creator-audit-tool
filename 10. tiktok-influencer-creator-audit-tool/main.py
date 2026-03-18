import os
import json
import gspread
from apify_client import ApifyClient
from dotenv import load_dotenv # pip install python-dotenv

load_dotenv()

# AMBIL DARI SYSTEM (Bukan ditulis manual)
APIFY_TOKEN = os.getenv('APIFY_TOKEN')
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

# LOGIKA UNTUK GOOGLE CREDENTIALS (Sangat Penting untuk GitHub Actions/Heroku)
google_creds_json = os.getenv('GOOGLE_APPLICATION_CREDENTIALS_JSON')

if google_creds_json:
    # Jika di Cloud (GitHub Actions), baca dari teks JSON di secret
    creds_dict = json.loads(google_creds_json)
    gc = gspread.service_account_from_dict(creds_dict)
else:
    # Jika di laptop sendiri, pakai file lokal
    gc = gspread.service_account(filename='credentials.json')

sh = gc.open_by_key(SPREADSHEET_ID)
worksheet = sh.get_worksheet(0)

def calculate_sonic_score(videos):
    if not videos: return 0
    scores = []
    for v in videos[:15]:
        st = v.get('stats') or v.get('videoStats') or v.get('video', {}).get('stats') or v
        try:
            sh = int(st.get('shareCount') or st.get('share_count') or 0)
            sa = int(st.get('collectCount') or st.get('collect_count') or 0)
            co = int(st.get('commentCount') or st.get('comment_count') or 0)
            li = int(st.get('diggCount') or st.get('digg_count') or 0)
            vi = int(st.get('playCount') or st.get('play_count') or 0)
            if li > 0 or vi > 0:
                scores.append((sh * 5) + (sa * 4) + (co * 2) + (li * 1) + (vi * 0.1))
        except: continue
    return float(pd.Series(scores).median()) if scores else 0

def run_pipeline():
    print(f"🚀 Memulai Pipeline V21 (Full Column Mode)...")
    records = worksheet.get_all_records()
    
    for i, row in enumerate(records, start=2):
        username = str(row.get('Username', '')).strip().replace('@', '')
        if not username: continue
        
        print(f"\n🔎 Processing: @{username}...")
        try:
            run_input = {"profiles": [f"https://www.tiktok.com/@{username}"], "resultsPerPage": 15}
            run = client.actor("clockworks/tiktok-profile-scraper").call(run_input=run_input)
            results = list(client.dataset(run["defaultDatasetId"]).iterate_items())

            if results:
                data = results[0]
                videos = data.get('latestPosts') or data.get('posts') or results
                author = data.get('authorMeta') or data.get('author') or {}
                
                # 1. Ambil Data Dasar
                followers = author.get('fans') or author.get('followerCount') or 0
                score = calculate_sonic_score(videos)
                
                # 2. Hitung Kolom Tambahan (Cost & ROI)
                # Misal: Harga per score adalah Rp 150
                estimated_cost = score * 150 
                roi_value = "High" if score > 1000000 else "Medium"
                
                # 3. Tentukan Status
                if score > 1000000: status = "🔥 Viral"
                elif score > 500000: status = "✅ Stabil"
                else: status = "⚠️ Potensial"

                # 4. UPDATE SEMUA KOLOM (B, C, D, E, F)
                # B: Followers, C: Score, D: Status, E: Cost, F: ROI
                payload = [[followers, round(score, 2), status, f"Rp{int(estimated_cost):,}", roi_value]]
                worksheet.update(f"B{i}:F{i}", payload)
                
                print(f"✅ @{username} UPDATED! Score: {round(score, 2)} | Status: {status}")
            
            time.sleep(3) # Jeda agar tidak terkena limit
        except Exception as e:
            print(f"❌ Gagal pada @{username}: {e}")

if __name__ == "__main__":
    run_pipeline()
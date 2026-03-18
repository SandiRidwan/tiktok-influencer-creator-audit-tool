import gspread
from google.oauth2.service_account import Credentials

# 1. SETUP CREDENTIALS
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
# Ganti 'credentials.json' dengan nama file JSON kamu
creds = Credentials.from_service_account_info(
    gspread.auth.service_account(filename='credentials.json').auth_info, 
    scopes=scope
)
gc = gspread.authorize(creds)

def create_sonic_dummy_sheet(user_email):
    try:
        # 2. BUAT SPREADSHEET BARU
        sheet_name = "SONIC_Influencer_CRM_Dummy"
        sh = gc.create(sheet_name)
        print(f"✅ Berhasil membuat file: {sheet_name}")
        print(f"🔗 Spreadsheet ID: {sh.id}")

        # 3. SETUP HEADER & DATA AWAL
        worksheet = sh.get_worksheet(0)
        headers = [
            "Username", "Followers", "Median Score", 
            "Status", "Cost", "ROI", "Email"
        ]
        
        # Contoh Username untuk Testing Portfolio
        dummy_rows = [
            headers,
            ["mrbeast", "", "", "", "", "", ""],
            ["khaby.lame", "", "", "", "", "", ""],
            ["zachking", "", "", "", "", "", ""],
            ["bellapoarch", "", "", "", "", "", ""],
            ["addisonre", "", "", "", "", "", ""]
        ]

        worksheet.update('A1', dummy_rows)
        
        # Format Header jadi Bold
        worksheet.format("A1:G1", {"textFormat": {"bold": True}})

        # 4. SHARE KE EMAIL KAMU (Agar muncul di Google Drive kamu)
        sh.share(user_email, perm_type='user', role='editor')
        print(f"📨 File telah dibagikan ke: {user_email}")
        print("🚀 Silakan cek Google Drive 'Shared with me' kamu!")

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    # GANTI DENGAN EMAIL KAMU SENDIRI
    MY_EMAIL = "sandyzvoster@gmail.com" 
    create_sonic_dummy_sheet(MY_EMAIL)
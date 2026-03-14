import uuid

def generate_config():
    # ID NextDNS của bạn
    nextdns_id = "d1b656"
    server_url = f"https://dns.nextdns.io/{nextdns_id}"
    
    # Các ID duy nhất để Apple nhận diện profile mới
    payload_uuid = str(uuid.uuid4()).upper()
    profile_uuid = str(uuid.uuid4()).upper()

    # Danh sách domain tối ưu bạn đã chọn
    domains = [
        "*.revenuecat.com",
        "*.v.locket.camera",
        "*.sandbox.itunes.apple.com",
        "*.buy.itunes.apple.com",
        "*.app-support.revenuecat.com",
        "*.purchase.locket.camera",
        "*.api.revenuecat.com"
    ]
    
    domain_xml = "\n".join([f"                    <string>{d}</string>" for d in domains])

    config_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>DNSSettings</key>
            <dict>
                <key>DNSProtocol</key>
                <string>HTTPS</string>
                <key>ServerAddresses</key>
                <array>
                    <string>45.90.28.0</string>
                    <string>45.90.30.0</string>
                </array>
                <key>ServerURL</key>
                <string>{server_url}</string>
                <key>SupplementalMatchDomains</key>
                <array>
{domain_xml}
                </array>
            </dict>
            <key>PayloadDescription</key>
            <string>DNS mã hóa để đóng băng Locket Gold và Anti-Revoke.</string>
            <key>PayloadDisplayName</key>
            <string>Locket VIP Freeze DNS (NextDNS)</string>
            <key>PayloadIdentifier</key>
            <string>com.apple.dnsSettings.managed.{nextdns_id}</string>
            <key>PayloadType</key>
            <string>com.apple.dnsSettings.managed</string>
            <key>PayloadUUID</key>
            <string>{payload_uuid}</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDescription</key>
    <string>Hồ sơ đóng băng bản quyền Locket Gold và chống thu hồi chứng chỉ.</string>
    <key>PayloadDisplayName</key>
    <string>💛 Locket Gold VIP (Freeze)</string>
    <key>PayloadIdentifier</key>
    <string>com.yourname.dns.freeze</string>
    <key>PayloadOrganization</key>
    <string>NextDNS Custom</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>{profile_uuid}</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>"""
    
    with open("dns.mobileconfig", "w", encoding="utf-8") as f:
        f.write(config_content)
    print("✅ Đã tạo file dns.mobileconfig thành công!")

if __name__ == "__main__":
    generate_config()

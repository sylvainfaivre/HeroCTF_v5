KEY = b"\xd2\x57\x4d\x5e\xcf\x67\x82\x53"
STRANGE = b"\x81\x63\x34\x01\x87\x54\xee\x1f\xe2\x08\x39\x6e\x90\x0a\xdb\x0c\xbe\x66\x39\x2a\xa3\x54\xdd\x15\x80\x66\x7e\x10\x8b\x46\xa3"
FLAG = ""

for i in range(len(STRANGE)):
	FLAG += chr( STRANGE[i] ^ KEY[i % len(KEY)] )

print("[+] Flag: Hero{" + FLAG + "}")
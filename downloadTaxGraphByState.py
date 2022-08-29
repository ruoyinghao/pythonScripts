
import ssl
import urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North-Carolina", "North-Dakota", "Nebraska", "New-Hampshire", "New-Jersey", "New-Mexico", "Nevada", "New-York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode-Island", "South-Carolina", "South-Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West-Virginia", "Wyoming"]
for state in stateNames:
	try:
		with urllib.request.urlopen("https://itep.sfo2.digitaloceanspaces.com/"+state+"-total-graph.jpg", context=ctx) as u, open(state+".jpg", 'wb') as f:
			f.write(u.read())
	except:
		print("cannot download tax graph for state "+state)
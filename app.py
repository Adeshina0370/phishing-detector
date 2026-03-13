import streamlit as st

# 3MTT Cybersecurity Project
st.set_page_config(page_title="CyberGuard Detector", page_icon="🛡️")

st.title("🛡️ CyberGuard: Phishing Link Detector")
st.write("A 3MTT Cybersecurity Awareness Tool for Financial Inclusion.")

# User Input
url = st.text_input("Paste the website URL here to check for red flags:").lower()

# Red Flag Keywords
red_flags = ['bit.ly', 'secure-login', 'login', 'update-account', 
             'bank-verification', 'free-airtime', 'verify-bvn']

if st.button("Scan for Threats"):
    if url == "":
        st.warning("Please enter a URL first!")
    else:
        # Check for flags
        found_flags = [flag for flag in red_flags if flag in url]
        
        if found_flags:
            st.error(f"⚠️ DANGER: This looks like a phishing link!")
            st.info(f"Red flags detected: {', '.join(found_flags)}")
        else:
            st.success("✅ This link appears safe based on our current database.")

st.divider()
st.caption("Developed by a 3MTT Cybersecurity Fellow | Osogbo, Osun State")

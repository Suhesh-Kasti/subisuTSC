import tkinter as tk
import ttkthemes
from tkinter import ttk
from tkinter import PhotoImage
from ttkbootstrap import Style

# Window create
window = tk.Tk()
window.title("TSC Playground")
window.geometry('1200x800')

# Set initial theme
current_theme = "journal"


# Set style
style = Style(theme=current_theme)
style.configure('TButton', padding=(0,0))

# Top Frame
top_frame = ttk.Frame(window)
top_frame.pack(side='top', fill='x')

# Combo Box
problems = ('Slow Browsing','Internet not working', 'No signal without logo', 'Router Configuration', 'Secondary Router', 'Network Error')
selected = tk.StringVar(value = problems[0])
select_problems= ttk.Combobox(master = top_frame, textvariable = selected, width=20)
select_problems['values'] = problems
select_problems.pack(side='left', padx=10, pady=10)

# Theme Button Frame
theme_button_frame = ttk.Frame(window)
theme_button_frame.pack(side='left', fill='y')

# Theme Button
def change_theme():
    global current_theme
    if current_theme == "journal":
        style.theme_use("darkly")
        current_theme = "darkly"
        theme_button.config(text="Light")
    else:
        style.theme_use("journal")
        current_theme = "journal"
        theme_button.config(text="Dark")

theme_button = ttk.Button(master=theme_button_frame, text="Dark", command=change_theme)
theme_button.pack(side='bottom', pady=10)

# Button Frame
button_frame = ttk.Frame(window)
button_frame.pack(side='left', fill='y', padx=10)

# Buttons
button_width = 20
button_padx = 10
button_pady = 10

steps_button = ttk.Button(master=button_frame, text="Solution Steps", style='primary.TButton', width=button_width, command=lambda: theFunc(selected, 'Solution Steps'))
steps_button.pack(side='top', pady=button_pady)

causes_button = ttk.Button(master=button_frame, text="Causes", style='primary.TButton', width=button_width, command=lambda: theFunc(selected, 'Causes'))
causes_button.pack(side='top', pady=button_pady)

techterms_button = ttk.Button(master=button_frame, text="Technical Terms", style='primary.TButton', width=button_width, command=lambda: theFunc(selected, 'Technical Terms'))
techterms_button.pack(side='top', pady=button_pady)

more_button = ttk.Button(master=button_frame, text="Learn some more", style='primary.TButton', width=button_width, command=lambda: theFunc(selected, 'Learn some more'))
more_button.pack(side='top', pady=button_pady)

# Output Text Box
output_box = tk.Text(master=window, height=100, width=int(window.winfo_width() * 0.9), font=('Roboto', 16), state=tk.DISABLED)
output_box.pack(side='right', fill='both', expand=True)



##############################################################################################################################################################
#################################Slow Internet Part Starts Here #############################################################################################
##############################################################################################################################################################

def slownet_solution():
    the_solution_slownet='''
    Step 1: Check the optical power(-16 to -27).

    Step 2: Check the session then reboot the client side ONU if there is long session.
    (*Note: If the client has cablenet, there might be no session displayed).

    Step 3: In session tab if the bandwidth consumption is high check if FUP is applied.
    If yes, forward the call to sales department with proper remarks.

    Step 4: Try changing channels and channel bandwidth. 
    Flush if any manually added DNS exists.

    Step 5: If the issues is with some particular app or website, try changing IP mode. 
    (Network > WAN > IP mode)
    If a particular site is not working try pinging the site. --- Eg. ping google.com -t
    (*Note: Don't use just the IPv6 one as the IP mode as it might introduce more issues than fix.)

    Step 6: If the client just has problems with the calls or CCTV cameras. Check the firewall of the ONU. 
    Security > Firewall > Disabled). 
    If it is on high/low calls in online sevices and CCTV videos may not work.

    Step 7: Rebooting the client's devices(smartphones, Tvs) might help.

    Step 8: If the client has a secondary router, you might need to log into the router, find an option called DHCP server and disable it.

    Step 9: If nothing helps resetting the ONU might solve the problem.

    Step 10: Raise a ticket to TSC open or L1/Rf team in accordance to client's request with proper remarks.
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, the_solution_slownet)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again


def slownet_terms():
    terms_slownet='''
    1. Channels =>
                Wi-Fi works by propagating data through a certain frequency radio waves. Wifi channels are like different lanes on a highway. Just as multiple cars can drive on a highway at the same time, multiple devices can transmit data on the same Wifi frequency at the same time. Just as cars can switch lanes to avoid congestion or take a faster route, Wifi devices can switch channels to find the least congested and fastest channel. It's important to note that Wifi channels can overlap and interfere with each other, especially if they are close in frequency. This is like two cars trying to change lanes at the same time and causing an accident.

    2. IP Modes =>
                IP modes are versions of Internet Protocol(IP). There are two of them IPv4 and IPv6. IPv4 is older but most commonly used mode whereas IPv6 is newer mode but not yet widely adopted. Sometimes certain websites may not be compatible with IPv6 whereas most if not all of the sites and applications support IPv4.

    3. Ping => 
               Ping is a simple networking utility that helps diagnose network connectivity issues and troubleshoot problems between devices on a network. Ping measures two things: latency and packet loss. Latency refers to the time it takes for the message to travel from your computer to the other device and back. Packet loss refers to the number of messages that don't make it to the other device or don't receive a response.

    4. DNS => 
                Domain Naming System is like a phonebook for the internet. It's a system that translates website names, like www.google.com, into IP addresses, like 216.58.194.174. It is because of DNS you don't have to memorize the IP address of each site rather just a name is enough.

    5. DHCP => 
                Each of the devices needs an IP address to be able to use the internet. Dynamic Host Control Protocol is responsible for allocating IP addresses to devices dynamically. 
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, terms_slownet)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again

def slownet_cause():
    the_cause_slownet='''
    1. Optical power may cause instability in the connection and also frequent disconnection.
        
    2. Longer sessions may cause the connections to slow down.
        
    3. Channel collisions usually cause speed degradation in Wi-Fi speed but the they don't affect ethernet connections.

    4. Sometimes if the client has a secondary router, having DHCP enabled on the secondary router may cause issues like some specific sites and applications not functioning in particular phones but working in other phones.
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, the_cause_slownet)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again

    

def slownet_more():
    more_slownet='''
    You should not reset the ONUs with static IP

    VLAN for IPTV - 1619
    VLAN for ACS - 1991
    VLAN for static IP - 375, 1202, 1810
    VLAN IDs For Various OLTs

    
        '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, more_slownet)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again


##############################################################################################################################################################
################################# No Internet Part Starts Here ###############################################################################################
##############################################################################################################################################################


def nonet_solution():
    the_solution_nonet='''
    Step 1: Check if the client's Data Service Status and Acoount Status is Active.
    If the account is active, check for Loss of Signal and Port Down 

    Step 2: Check the session. If there is no Port Down or LOS but no session is displayed, check if the MAC in S3 matches the MAC in AMS/DE/Horizon.
    (*Note: If the client has cablenet, there might be no session displayed).

    Step 3:  If the MAC is correct but there is no session displayed check for Access Log. If there is frequent access log provide the VLAN ID and username to the immediate supervisor.
    (*Note: If the client has just paid there might be no session and no sccess log. Rebooting the ONU from client side or AMS usually solves this issue)

    Step 4: If the client is unable to find the SSID of his connection, check if the WLAN light in client's ONU is on.
    if the light is OFF, press the button that says WLAN in the ONU.
    if the light is ON, search if there is a SSID that starts with ALHN-{last four digits of client's ONU ID}, use the WIFI Key given at bottom of ONU to connect to this network.

    Step 5: Check if the internet is not working on all client's devices or just a particular device. 
    Something might be wrong with the client's device itself.

    Step 5: Rebooting the client's devices(smartphones, Tvs) might help.

    Step 6: If the client has a secondary router, you might need to log into the router, find an option called DHCP server and disable it.

    Step 7: If nothing helps resetting the ONU might solve the problem.

    Step 8: Raise a ticket to TSC open or L1/Rf team in accordance to client's request with proper remarks.
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, the_solution_nonet)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again


def nonet_terms():
    terms_nonet='''
    1. SSID(Service Set Identifier) =>
                This is essentially just the name given to the Wi-Fi Network.

    2. ONU(Optical Network Unit) =>
                A device that works as the modem for optical networks. This device is responsible for converting digital signal to analog. ONU doesn't necessarily mean a router but the device SUBISU provides has a built-in ONU, router and switch.

    3. OLT(Optical Line Terminal) => 
               It is a device that sits at the receiving end of the Optical Network. This has all the end cables and is responsible for internet flowing to the DB boxes through its ports.

    4. DB(Distribution Box)=> 
                The box that you might have seen ISPs setup in poles that has the other end of the wires connected to your ONU.  

    5. Port => 
                Not necessarily meaning the area, port simply mean the ports in an OLT. Port down doesn't essentially mean the whole area is down but rather the connections from a specific port is down. Since the same port serves internet to the same area, area down can be interchangebly be used for port down.

    6. VLAN ID=>
            Specific OLT's are provided with numbers as their identifiers which is the VLAN ID. VLANs are logical/software based seperation of various ports in a switch. Ports of a core/distribution layer switches are segregated using this technique to seperate them. 
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, terms_nonet)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again

def nonet_cause():
    the_cause_nonet='''
    1. Loss of signal, port down, OLT down is usually the cause for internet not working. 
    Optical power may cause instability in the connection and also frequent disconnection.
        
    2. Longer sessions may cause the connections to slow down and make it feel like the internet is not working.
        
    3. No session, frequent access log also cause internet to not work.

    4. Sometimes if the client has a secondary router, having DHCP enabled on the secondary router may cause issues like some specific sites and applications not functioning.
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, the_cause_nonet)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again

    

def nonet_more():
    more_nonet='''
    You should not reset the ONUs with static IP

    VLAN for IPTV - 1619
    VLAN for ACS - 1991
    VLAN for static IP - 375, 1202, 1810
    VLAN IDs For Various OLTs

    
        '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, more_nonet)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again




##############################################################################################################################################################
################################# No Signal No logo Part Starts Here #########################################################################################
##############################################################################################################################################################


def nologo_solution():
    the_solution_nologo='''
    Step 1: Check if the cables are cables are connected properly. The HDMI/AV cables have to be properly connected.

    Step 2: Check if the source is properly selected. In the TV's remote(not clear tv's) check for a button that says "Input" or "Source" or "TV/AV" or "HDMI" or "picture of a arrow beside a rectangle". Select proper source.

    Step 3: Rebooting the client's TV and STB might help.

    Step 4: Raise a ticket to TSC open or L1/Rf team in accordance to client's request.
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, the_solution_nologo)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again


def nologo_terms():
    terms_nologo='''
    1. K K add garum yesma??
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, terms_nologo)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again

def nologo_cause():
    the_cause_nologo='''
    1. Loose cables cause the TV to not be able to receive any output from the STB.
        
    2. Incorrect source being chosen confuses the TV.
        
    3. 
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, the_cause_nologo)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again

    

def nologo_more():
    pass

##############################################################################################################################################################
################################# ONU configuration part Starts Here ############################################################################
##############################################################################################################################################################


def onu_solution():
    the_solution_onu='''
    Step 1: 
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, the_solution_onu)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again


def onu_terms():
    terms_onu='''
    1. 
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, terms_onu)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again

def onu_cause():
    the_cause_onu='''
    1. The need of longer range makes client want a secondary router
        
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, the_cause_onu)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again

    

def onu_more():
    pass

#############################################################################################################################################################
################################# Secondary router configuration part Starts Here ############################################################################
##############################################################################################################################################################


def second_solution():
    the_solution_second='''
    Step 1: 
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, the_solution_second)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again


def second_terms():
    terms_second='''
    1. 
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, terms_second)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again

def second_cause():
    the_cause_second='''
    1. The need of longer range makes client want a secondary router
        
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, the_cause_second)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again

    

def second_more():
    pass


##############################################################################################################################################################
################################# Network Error Part Starts Here #########################################################################################
##############################################################################################################################################################


def network_solution():
    the_solution_network='''
    Step 1: Check if the ethernet cables on both the router and STB is properly connected. If they are, the light on both the STB and the port in router should be glowing.
    Step 2: Check if there is MAC displayed on the 1619 vlan either from DE or horizon or AMS. 
    If not, from ACS check if the port to which the cable is connected is bridged. 
    In ACS =>
        The "false" denotes Bridged mode and "true" denotes route mode.
    In GPON gateway=>
        Goto Network > LAN where port1, port2 are given. The port in which the ethernet cable is connected should have mode as bridged.

    Step 3: After changing the port's mode, reboot the STB and it must open with the message "STB initializing".
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, the_solution_network)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again


def network_terms():
    terms_network='''
    1. Bridged mode =>
                When the port is set to bridged, the device connected to that port receives its own public IP unlike in route mode where the DHCP provides a private IP address.

    2. Public IP =>
                The IP address that can be accessed directly over the internet and is assigned to your network router by your internet service provider (ISP). VPN changes this IP address. This is the IP that publicly identifies your connection.  

    3.Private IP =>
                A private IP address is a range of non-internet facing IP addresses used in an internal network. It is provided by the DHCP server inside the ONU.
    4.STB(Set-top box) =>
                

    5. DTV(Digital TV) =>
                Old type of STB. This doesn't use any form of IP address.

    6. DTI/IPTV =>
                New type of STB that uses IP address 
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, terms_network)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again

def network_cause():
    the_cause_network='''
    1. Optical power may cause instability in the connection and also frequent disconnection.
        
    2. Longer sessions may cause the connections to slow down.
        
    3. Channel collisions also lead to slowness in Wi-Fi speed but the they don't affect ethernet connections.

    4. Sometimes if the client has a secondary router, having DHCP enabled on the secondary router may cause issues like some specific sites and applications not functioning in particular phones but working in other phones.
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, the_cause_network)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again

    

def network_more():
    pass



##############################################################################################################################################################
################################# This function is responsible for button selection and output display #########################################################
##############################################################################################################################################################



def theFunc(selected, from_button):
    if selected.get() == 'Slow Browsing' and from_button == 'Solution Steps':
        slownet_solution()
    if selected.get() == 'Slow Browsing' and from_button == 'Causes':
        slownet_cause()
    if selected.get() == 'Slow Browsing' and from_button == 'Technical Terms':
        slownet_terms()
    if selected.get() == 'Slow Browsing' and from_button == 'Learn some more':
        slownet_more()
    if selected.get() == 'Internet not working' and from_button == 'Solution Steps':
        nonet_solution()
    if selected.get() == 'Internet not working' and from_button == 'Causes':
        nonet_cause()
    if selected.get() == 'Internet not working' and from_button == 'Technical Terms':
        nonet_terms()
    if selected.get() == 'Internet not working' and from_button == 'Learn some more':
        nonet_more()
    if selected.get() == 'No signal without logo' and from_button == 'Solution Steps':
        nologo_solution()
    if selected.get() == 'No signal without logo' and from_button == 'Causes':
        nologo_cause()
    if selected.get() == 'No signal without logo' and from_button == 'Technical Terms':
        nologo_terms()
    if selected.get() == 'No signal without logo' and from_button == 'Learn some more':
        nologo_more()
    if selected.get() == 'Router Configuration' and from_button == 'Solution Steps':
        onu_solution()
    if selected.get() == 'Router Configuration' and from_button == 'Causes':
        onu_cause()
    if selected.get() == 'Router Configuration' and from_button == 'Technical Terms':
        onu_terms()
    if selected.get() == 'Router Configuration' and from_button == 'Learn some more':
        onu_more()
    if selected.get() == 'Secondary Router' and from_button == 'Solution Steps':
        second_solution()
    if selected.get() == 'Secondary Router' and from_button == 'Causes':
        second_cause()
    if selected.get() == 'Secondary Router' and from_button == 'Technical Terms':
        second_terms()
    if selected.get() == 'Secondary Router' and from_button == 'Learn some more':
        second_more()
    if selected.get() == 'Network Error' and from_button == 'Solution Steps':
        network_solution()
    if selected.get() == 'Network Error' and from_button == 'Causes':
        network_cause()
    if selected.get() == 'Network Error' and from_button == 'Technical Terms':
        network_terms()
    if selected.get() == 'Network Error' and from_button == 'Learn some more':
        network_more()

##############################################################################################################################################################
################################# I know this function can be implemented more efficiently  using for-loop ###################################################
################################# But when I made this I had no idea and now I am too lazy to fix for regidness###############################################
##############################################################################################################################################################

    
# get the window
window.mainloop()

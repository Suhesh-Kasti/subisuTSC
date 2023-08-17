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
problems = ('Slow Browsing','Internet not working', 'No signal without logo', 'Router Configuration', 'Secondary Router')
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





def slownet_solution():
    the_solution_slownet='''
    Step 1: Check the optical power(-16 to -27).

    Step 2: Check the session then reboot the client side ONU.
    (*Note: If the client has cablenet, there might be no session displayed).

    Step 3: Try changing channels and channel bandwidth. 
    Flush if any manually added DNS exists.

    Step 4: If the issues is with some particular app or website, try changing IP mode.
    (Network > WAN > IP mode)

    Step 5: Rebooting the client's device might help.

    Step 6: If the client has a secondary router, you might need to log into the router, find an option called DHCP server and disable it.

    Step 7: If nothing helps resetting the ONU might solve the problem.

    Step 8: Raise a ticket to TSC open or L1/Rf team in accordance to client's request.
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
    1. Optical power may cause instability in the connection and also sluggishness.
        
    2. Longer sessions may cause the connections to slow down.
        
    3. Channel collisions also lead to slowness in Wi-Fi speed but the they don't affect ethernet connections.

    4. Sometimes if the client has a secondary router, having DHCP enabled on the secondary router may cause issues.
    '''
    output_box.config(state=tk.NORMAL)  # make the widget editable
    output_box.delete('1.0', tk.END)  # clear previous content
    output_box.insert(tk.END, the_cause_slownet)
    output_box.config(state=tk.DISABLED)  # make the widget non-editable again

    

def slownet_more():
    pass

def theFunc(selected, from_button):
    if selected.get() == 'Slow Browsing' and from_button == 'Solution Steps':
        slownet_solution()
    if selected.get() == 'Slow Browsing' and from_button == 'Causes':
        slownet_cause()
    if selected.get() == 'Slow Browsing' and from_button == 'Technical Terms':
        slownet_terms()
    if selected.get() == 'Slow Browsing' and from_button == 'Learn some more':
        slownet_more()
    if selected.get() == 'Internet not Working' and from_button == 'Solution Steps':
        slownet_solution()
    if selected.get() == 'Internet not Working' and from_button == 'Causes':
        slownet_cause()
    if selected.get() == 'Internet not Working' and from_button == 'Technical Terms':
        slownet_terms()
    if selected.get() == 'Internet not Working' and from_button == 'Learn some more':
        slownet_more()
    if selected.get() == 'No signal without logo' and from_button == 'Solution Steps':
        slownet_solution()
    if selected.get() == 'No signal without logo' and from_button == 'Causes':
        slownet_cause()
    if selected.get() == 'No signal without logo' and from_button == 'Technical Terms':
        slownet_terms()
    if selected.get() == 'No signal without logo' and from_button == 'Learn some more':
        slownet_more()
    if selected.get() == 'Router Configuration' and from_button == 'Solution Steps':
        slownet_solution()
    if selected.get() == 'Router Configuration' and from_button == 'Causes':
        slownet_cause()
    if selected.get() == 'Router Configuration' and from_button == 'Technical Terms':
        slownet_terms()
    if selected.get() == 'Router Configuration' and from_button == 'Learn some more':
        slownet_more()
    if selected.get() == 'Secondary Router' and from_button == 'Solution Steps':
        slownet_solution()
    if selected.get() == 'Secondary Router' and from_button == 'Causes':
        slownet_cause()
    if selected.get() == 'Secondary Router' and from_button == 'Technical Terms':
        slownet_terms()
    if selected.get() == 'Secondary Router' and from_button == 'Learn some more':
        slownet_more()

    
# get the window
window.mainloop()

import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
    
    ip = input("human : ")
    op = kernel.respond(ip)
    print ("bot : ",op)

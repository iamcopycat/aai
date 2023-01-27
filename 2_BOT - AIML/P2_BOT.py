import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std2-startup.xml")
kernel.respond("load prac 2")

# Press CTRL-C to break this loop
while True:
    input_text = input("> Human : ")
    response = kernel.respond(input_text)
    print("> BOT : ", response)

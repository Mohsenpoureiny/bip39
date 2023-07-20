import qrcode

passphrasel = ['deny', 'advice', 'scene', 'scan', 'proud', 'key', 'found', 'echo', 'color', 'wire', 'rack', 'torch']


img = qrcode.make(' '.join(passphrasel))
 
img.save('pass.png')
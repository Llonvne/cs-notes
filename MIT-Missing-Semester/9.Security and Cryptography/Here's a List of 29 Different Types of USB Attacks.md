# Here's a List of 29 Different Types of USB Attacks

A) By reprogramming the USB device's internal microcontroller. The device looks like a particular USB device (e.g.: charger), but carries out the operations of another (e.g.: keyboard —injects keystrokes).
通过重新编程USB设备的内部微控制器。该设备外观看起来像一个特定的USB设备（例如：充电器），但执行另一个设备的操作（例如：键盘-注入按键）。
B1) By reprogramming the USB device's firmware to execute malicious actions (such as malware downloading, data exfiltration, etc.).
通过重新编程USB设备的固件来执行恶意操作（如下载恶意软件、数据泄露等）。
B2) By not reprogramming USB device firmware, but leveraging flaws in how operating systems normally interact with USB protocols/standards.
通过不重新编程USB设备固件，而是利用操作系统与USB协议/标准的交互中的缺陷。
C) USB-based electrical attacks.
C) 基于USB的电攻击。

## Reprogrammable microcontroller USB attacks 可重新编程的微控制器USB攻击

1) [Rubber Ducky](https://shop.riftrecon.com/products/rubberducky) - a commercial keystroke injection attack platform released in 2010. Once connected to a host computer, the Rubber Ducky poses as a keyboard and injects a preloaded keystroke sequence.

橡胶鸭 - 一种商业键盘注入攻击平台，于2010年发布。一旦连接到主机计算机，橡胶鸭会伪装成键盘并注入预加载的按键序列。

2) [PHUKD/URFUKED attack platforms](http://www.irongeek.com/i.php?page=security/programmable-hid-usb-keystroke-dongle) - similar to Rubber Ducky, but allows an attacker to select the time when it injects the malicious keystrokes.
3) PHUKD/URFUKED攻击平台 - 类似于橡皮鸭，但允许攻击者选择注入恶意按键的时间。

3) [USBdriveby](http://samy.pl/usbdriveby/) - provides quick covert installation of backdoors and overriding DNS settings on an unlocked OS X host via USB in a matter of seconds by emulating an USB keyboard and mouse.

USBdriveby - 通过模拟USB键盘和鼠标，在几秒钟内通过USB在未锁定的OS X主机上进行快速隐蔽安装后门和覆盖DNS设置。

4) [Evilduino](http://hackwhiz.com/2015/03/evilduino-usb-hack-tool/) - similar to PHUKD/URFUKED, but uses Arduino microcontrollers instead of Teensy. Also works by emulating a keyboard/mouse and can send keystrokes/mouse cursor movements to the host according to a preloaded script.
5) Evilduino - 类似于PHUKD/URFUKED，但使用Arduino微控制器而不是Teensy。同样通过模拟键盘/鼠标工作，并可以根据预加载的脚本向主机发送按键/鼠标光标移动。
6) Unintended USB channel - a [proof of concept (POC) USB hardware trojan](http://ieeexplore.ieee.org/document/5319005/authors?part=1) that exfiltrates data based on unintended USB channels (such as using USB speakers to exfiltrate data).
7) 非预期的USB通道 - 一个概念验证（POC）的USB硬件木马，根据非预期的USB通道（例如使用USB扬声器来窃取数据）窃取数据。
8) [TURNIPSCHOOL (COTTONMOUTH-1)](http://www.nsaplayset.org/turnipschool) - a hardware implant concealed within a USB cable. Developed by the NSA.
9) TURNIPSCHOOL（COTTONMOUTH-1）- 一种隐藏在USB电缆中的硬件植入物。由美国国家安全局开发。
10) [RIT attack via USB mass storage](https://pdfs.semanticscholar.org/70d7/d873c72d0db9968650ad359c6ef915ffbb42.pdf) - attack described in a research paper. It relies on changing the content of files while the USB mass storage device is connected to a victim's computer.
11) 通过USB大容量存储设备进行的RIT攻击 - 这是一篇研究论文中描述的攻击。它依赖于在USB大容量存储设备连接到受害者的计算机时改变文件内容。
12) Attacks on wireless USB dongles - a category of attacks first explored with the release of the [KeySweeper](https://samy.pl/keysweeper/) attack platform by Samy Kamkar, a tool that covertly logs and decrypts keystrokes from many Microsoft RF wireless keyboards.

对无线USB dongles的攻击 - 这是一类攻击，最早由Samy Kamkar发布的KeySweeper攻击平台进行探索，该工具可以秘密记录和解密许多微软RF无线键盘的按键记录。

9) [Default Gateway Override](https://srlabs.de/wp-content/uploads/2014/07/SRLabs-BadUSB-BlackHat-v1.pdf) - an attack that uses a microcontroller to spoof a USB Ethernet adapter to override DHCP settings and hijack local traffic.

默认网关覆盖 - 一种利用微控制器欺骗USB以太网适配器来覆盖DHCP设置并劫持本地流量的攻击。
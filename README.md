paste是一个命令行版本的贴代码到paste.ubuntu.com</br>
返回贴完代码的url</br>
参数1 文件名即文件路径</br>
参数2 poster</br>
参数3 代码格式，C是c，c++是cpp，文本是text，Python是python</br>
例如：python paste.py a.cpp UCU cpp</br>
我把这个配置进了vim，F4一键贴代码并且返回的url已经在剪贴板里非常好用，这里的.vimrc就是这个配置</br>(pbcopy是mac的配置，linux下可以改用xsel,ptUt是我做的软链接，可以随意改为其他命令名)</br> 
getpaste是一个命令行版本的根据url或者是paste.ubuntu.com的编号获得所贴内容的工具</br>
例如:</br>
python getpaste http://paste.ubuntu.com/11794787/ </br>
python getpaste 11794787 </br>
mac下配合pbcopy,pbpaste使用体验极佳
linux下可配合xsel使用<br>
目前getpaste只能用于get是plain text的代码<br>
至于,做软链接的Shell，例如<br>
chmod u+x paste.py<br>
ln -s (the_path_of_paste) /user/local/bin/ptUt<br>

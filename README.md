# python-
先后上传的两个文件大致介绍如下：
1.beautifulsoup.py 是利用多线程来爬取新笔趣阁上小说并分章节保存的脚本。
2.xbqgtoMP3.py 是单线程爬取新笔趣阁上的小说并转换成mp3格式保存的脚本。（单线程是因为免费的百度api会有QPS限制。单线程虽然慢点，但起码不用支付额外的
学习费用）
3.xbqgtoMP3Thread.py是对在运行的线程数进行一个限制，使用threading.Semaphore()对在运行的线程数进行一个限制，使用threading.Semaphore可以控制最多允许多少个线程同时进行，超出的部分自动等待，threading.Semaphore的使用只需要初始化，然后在自己新建的MyThread类的run()方法中用上下文管理形式，即可保证当开启新线程时，如果同时运行线程数会超过设置的最大值，则start等待不执行，直到前面的线程运行结束才可以开始。此处能兼容aip不会触发QPS限制的上限我没有测试过，又兴趣的同学可以自己测试一下(目前测试15没问题)。

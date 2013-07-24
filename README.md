hotdeal_automate
================

好康的自动化测试脚本,架构环境为 *selenium+python+webdriver*
具体安装过程见 [这里](http://www.cnblogs.com/ms_config/p/3205060.html)

###login_s.py 
测试登陆过程 第一个参数为测试员的email ,第二个测试员的密码
```js
{
    python login_s.py your email your password
}
```
###promo_s.py 
测试设计对白活动的过程 第一个参数为测试员的email ,第二个测试员的密码, 第三个为对白内容
```js
{
    python promo_s.py your email your password   dialog_content
}
```


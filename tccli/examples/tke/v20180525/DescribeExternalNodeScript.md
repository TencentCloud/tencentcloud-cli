**Example 1: 获取注册节点初始化脚本**

获取注册节点初始化脚本

Input: 

```
tccli tke DescribeExternalNodeScript --cli-unfold-argument  \
    --ClusterId cls-2isgxkje \
    --NodePoolId np-bnd1ybd4
```

Output: 
```
{
    "Response": {
        "Command": "wget --header=\"x-cos-token:tokenvalue\" 'http://example.cos.ap-guangzhou.myqcloud.com/user-pkgs%2Fcls-2isgxkje700000446531700000446531gz%2Fadd2tkectl?q-sign-algorithm=sha1&q-ak=xxxxx&q-sign-time=1773902065%3B1773905665&q-key-time=1773902065%3B1773905665&q-header-list=host%3Bx-cos-token&q-url-param-list=&q-signature=92db17c604be5987fc41524be89f9247afb34aee' -O add2tkectl-cls-2isgxkje-np-bnd1ybd4 && chmod +x add2tkectl-cls-2isgxkje-np-bnd1ybd4",
        "Link": "https://example.cos.ap-guangzhou.myqcloud.com/user-pkgs%2Fcls-2isgxkje700000446531700000446531gz%2Fadd2tkectl?q-sign-algorithm=sha1&q-ak=xxxx&q-sign-time=1773902065%3B1773905665&q-key-time=1773902065%3B1773905665&q-header-list=host%3Bx-cos-token&q-url-param-list=&q-signature=92db17c604be5987fc41524be89f9247afb34aee",
        "Token": "tokenvalue",
        "RequestId": "7b4dae36-4a1a-4583-9317-419851aef6b4"
    }
}
```


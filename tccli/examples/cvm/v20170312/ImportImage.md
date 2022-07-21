**Example 1: 导入镜像**

用户导入镜像。

Input: 

```
tccli cvm ImportImage --cli-unfold-argument  \
    --ImageUrl http://111-1251233127.cosd.myqcloud.com/Windows%20Server%202008%20R2%20x64a.vmdk \
    --ImageDescription sampleimage \
    --ImageName sample \
    --Architecture x86_64 \
    --OsType CentOS \
    --OsVersion 6
```

Output: 
```
{
    "Response": {
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
    }
}
```


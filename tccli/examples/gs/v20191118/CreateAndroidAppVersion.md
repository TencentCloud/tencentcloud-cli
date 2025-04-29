**Example 1: 创建安卓应用版本**

创建安卓应用版本

Input: 

```
tccli gs CreateAndroidAppVersion --cli-unfold-argument  \
    --AndroidAppId apk-ne70ubtu \
    --Command tar -zxvf test-1.0.X.tar.gz && cd test-1.0.X && ./install.sh \
    --UninstallCommand cd test-1.0.X && ./uninstall.sh \
    --DownloadUrl 
```

Output: 
```
{
    "Response": {
        "AndroidAppVersion": "1705458203832573301",
        "RequestId": "143c46a1-70f4-4371-8cc8-c30efef53c4e"
    }
}
```

**Example 2: 使用应用包下载链接创建安卓应用版本**

使用应用包下载链接创建安卓应用版本

Input: 

```
tccli gs CreateAndroidAppVersion --cli-unfold-argument  \
    --AndroidAppId apk-ne70ubtu \
    --DownloadUrl https://static.maoercdn.com/app/202312/29/MissEvan.apk
```

Output: 
```
{
    "Response": {
        "AndroidAppVersion": "1705458203832573301",
        "RequestId": "143c46a1-70f4-4371-8cc8-c30efef53c4e"
    }
}
```


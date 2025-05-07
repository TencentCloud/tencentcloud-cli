**Example 1: 修改安卓应用版本示例**



Input: 

```
tccli gs ModifyAndroidAppVersion --cli-unfold-argument  \
    --AndroidAppId apk-ne70ubtu \
    --AndroidAppVersion ver-a1b2c3 \
    --AndroidAppVersionName a1b2c3 \
    --Command tar -zxvf test-1.0.X.tar.gz && cd test-1.0.X && ./install.sh \
    --UninstallCommand cd test-1.0.X && ./uninstall.sh
```

Output: 
```
{
    "Response": {
        "RequestId": "143c46a1-70f4-4371-8cc8-c30efef53c4e"
    }
}
```


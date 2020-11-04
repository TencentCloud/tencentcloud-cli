**Example 1: 获取云托管代码上传url**

通过环境id,获得云托管代码上传url, 用来上传代码

Input: 

```
tccli tcb DescribeCloudBaseBuildService --cli-unfold-argument  \
    --EnvId cdnheader-v2a\
    --ServiceName nginx-test
```

Output: 
```
{
    "Response": {
        "Headers": [
            {
                "key": "Authorization",
                "value": "Basic aaaabase64"
            }
        ],
        "Url": "https://baozipi-generic.pkg.coding.net/coding_upgrade_date_SajgC/generic/hello.zip?version=1110282811",
        "PackageName": "nginx-test",
        "PackageVersion": "1001"
    }
}
```


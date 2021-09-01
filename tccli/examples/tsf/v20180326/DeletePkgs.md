**Example 1: 批量删除包**

删除应用application-6yogpwev下的包ID为pkg-c111a328、pkg-cb973b90等四个软件包。

Input: 

```
tccli tsf DeletePkgs --cli-unfold-argument  \
    --ApplicationId application-xxxxxxxx \
    --PkgIds pkg-xxxxxxx pkg-xxxxxxx1 pkg-xxxxxxxx pkg-xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "41bbd64c-1c82-4ea7-bda0-0c5ea33d6121"
    }
}
```


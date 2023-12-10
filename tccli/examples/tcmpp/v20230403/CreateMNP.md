**Example 1: demo**

demo

Input: 

```
tccli tcmpp CreateMNP --cli-unfold-argument  \
    --MNPName 测试小程序 \
    --MNPType 教育->在线教育,教育服务->教育平台,教育服务->素质教育 \
    --MNPIntro 学习强国 \
    --MNPDesc 学习强国 \
    --MNPIcon https://tcmpp-dev-renter-1258344699.cos.ap-guangzhou.tencentcos.cn/T1683257917UJWKPM/default/be20d614-230b-47fd-81b9-22994a9bd839_xx.png
```

Output: 
```
{
    "Response": {
        "Data": {
            "ResourceId": "abc"
        },
        "RequestId": "abc"
    }
}
```


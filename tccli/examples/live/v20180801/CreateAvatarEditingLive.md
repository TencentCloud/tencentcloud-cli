**Example 1: 创建实时编辑数字人**



Input: 

```
tccli live CreateAvatarEditingLive --cli-unfold-argument  \
    --ChannelId vidu_s2_editing_test_2 \
    --ImageUrl https://wsh-test-1303333058.cos.ap-guangzhou.myqcloud.com/change/2%E6%B1%89%E6%9C%8D.png \
    --EditingType virtual_tryon
```

Output: 
```
{
    "Response": {
        "ChannelId": "vidu_s2_editing_test_2",
        "LiveId": "1008224608114978816",
        "Status": "waiting",
        "RequestId": "0c104bce-d2f4-4363-b463-cf46fab5519e"
    }
}
```


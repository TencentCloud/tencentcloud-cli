**Example 1: 查看第三方节点列表**



Input: 

```
tccli tke DescribeExternalNodeScript --cli-unfold-argument  \
    --ClusterId cls-lm91rql0 \
    --NodePoolId np-0nwzqj10 \
    --Interface eth0 \
    --Name node1
```

Output: 
```
{
    "Response": {
        "RequestId": "48849133-f394-4c4c-9891-f013e209c025",
        "Link": "https://tke-edge-1253687700.cos.ap-guangzhou.myqcloud.com/user-pkgs%2Fcls-19zn81yu3321337994100018114712ap-guangzhou%2Fadd2tkectl?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDTeaJo55GyQgvzojguuSl24qNey3wa7NN%26q-sign-time%3D1618561008%3B1618564608%26q-key-time%3D1618561008%3B1618564608%26q-header-list%3Dx-cos-token%26q-url-param-list%3D%26q-signature%3D7994096869abf8492c0c6cbc68f93701bab7ac4f",
        "Token": "UAkOh6wCxzr8M8zf",
        "Command": "wget --header=\"x-cos-token:UAkOh6wCxzr8M8zf\" https://tke-edge-1253687700.cos.ap-guangzhou.myqcloud.com/user-pkgs%2Fcls-19zn81yu3321337994100018114712ap-guangzhou%2Fadd2tkectl?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDTeaJo55GyQgvzojguuSl24qNey3wa7NN%26q-sign-time%3D1618561008%3B1618564608%26q-key-time%3D1618561008%3B1618564608%26q-header-list%3Dx-cos-token%26q-url-param-list%3D%26q-signature%3D7994096869abf8492c0c6cbc68f93701bab7ac4f -O add2tkectl && chmod +x add2tkectl"
    }
}
```


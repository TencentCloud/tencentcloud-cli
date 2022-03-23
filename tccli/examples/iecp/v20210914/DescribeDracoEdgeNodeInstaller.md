**Example 1: 获取draco设备安装脚本**



Input: 

```
tccli iecp DescribeDracoEdgeNodeInstaller --cli-unfold-argument  \
    --SN SN2232323
```

Output: 
```
{
    "Response": {
        "RequestId": "115d57b3-6936-42a3-a9b7-1d84667c4e66",
        "OnlineInstallationCommand": "wget --header=\"x-cos-token:9h7Mq2zHoDK5mx3B\" https://tke-edge-1253687700.cos.accelerate.myqcloud.com/user-pkgs%2Fcls-9ab5x7749100009935455ap-guangzhou%2Fedgectl?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDUnpa4HDtIQHsDH4g15sOedLlvoQlpc8N%26q-sign-time%3D1647844231%3B1647847831%26q-key-time%3D1647844231%3B1647847831%26q-header-list%3Dx-cos-token%26q-url-param-list%3D%26q-signature%3D8345b0e5625d05bafa06bd2a898cf -O edgectl && chmod +x edgectl && ./edgectl install -n dddd"
    }
}
```


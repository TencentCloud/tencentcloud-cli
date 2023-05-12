**Example 1: 请求示例**

查询节点信息

Input: 

```
tccli redis DescribeInstanceNodeInfo --cli-unfold-argument  \
    --InstanceId crs-mufy7q15
```

Output: 
```
{
    "Response": {
        "Proxy": [
            {
                "NodeId": "de1d54148ed79f11c3b4a49c878b29c7218a6a30",
                "ZoneId": 100006
            },
            {
                "NodeId": "4b44ac3482e32ad1636b0d873f4fe795e1ace115",
                "ZoneId": 100006
            },
            {
                "NodeId": "524cc561f6621bc90d726dc62e15c66523754351",
                "ZoneId": 100006
            },
            {
                "NodeId": "5a0b7dfd340e8938762a3fabd390fed0e3635bb2",
                "ZoneId": 100006
            },
            {
                "NodeId": "71506b68e9ee8657b117846f66d66b8dd93a1344",
                "ZoneId": 100006
            },
            {
                "NodeId": "d4d3c819851952b01bd64e9ed7b3ada279b98ff7",
                "ZoneId": 100006
            },
            {
                "NodeId": "183a26e4ca59f98487276ce303ba50a2d71a423b",
                "ZoneId": 100006
            },
            {
                "NodeId": "002293180829fa0b2ab75b4ecd46d39194cabbfb",
                "ZoneId": 100006
            },
            {
                "NodeId": "6cd3f7b5cf412d1e93ab423c959c667e9ff6b75c",
                "ZoneId": 100006
            },
            {
                "NodeId": "52dd9608df1a0b8db6a28510866071f6638855bf",
                "ZoneId": 100006
            },
            {
                "NodeId": "6b62f8239e0851f8a2660cd13dd58bf171cb0f49",
                "ZoneId": 100006
            },
            {
                "NodeId": "6643b7242ad3c47c8b8622f28bf241db0a7b0dde",
                "ZoneId": 100006
            },
            {
                "NodeId": "dc78e5013a6cfd886eb16a49c2248b956551e77c",
                "ZoneId": 100004
            },
            {
                "NodeId": "d89e53a50448b3d61433317bc090625217cdeaf1",
                "ZoneId": 100004
            },
            {
                "NodeId": "156aebf190383685303ff68978c91adcd308ef27",
                "ZoneId": 100004
            },
            {
                "NodeId": "b8ebc56c5c346b6f79d75f81e6ee5d5f739c75f1",
                "ZoneId": 100004
            },
            {
                "NodeId": "ebbc08014c2c8c53132a541c7321dbf9cef8d09f",
                "ZoneId": 100004
            },
            {
                "NodeId": "e7c18f48e024bdd938a970a67fea207c6cf77138",
                "ZoneId": 100004
            },
            {
                "NodeId": "755d3a3ffc28786b92c2615bde8f17e37e861e57",
                "ZoneId": 100004
            },
            {
                "NodeId": "bb160769730dc46e8408c1d7ebddc8cdd6c1a0f8",
                "ZoneId": 100004
            },
            {
                "NodeId": "4ecab8b25acc46e6bd82dc469328a50fb9568656",
                "ZoneId": 100004
            },
            {
                "NodeId": "27bdbc76b6f714764fb48ff4ddc26db6a20796f5",
                "ZoneId": 100004
            },
            {
                "NodeId": "833f13e8d33ed1b5e8e87a935d0e48c4025af8c3",
                "ZoneId": 100004
            },
            {
                "NodeId": "81c2bd2f68215c5a5020fa900f481894e3b95eca",
                "ZoneId": 100004
            }
        ],
        "ProxyCount": 24,
        "Redis": [
            {
                "ClusterId": 0,
                "NodeId": "cc1e7c5ca61f52252df1ca6562db22e2af6eaa1f",
                "NodeRole": "master",
                "ZoneId": 100006
            },
            {
                "ClusterId": 0,
                "NodeId": "7b567e0bf382294e03ca88c33ef536f4a0412c7c",
                "NodeRole": "master",
                "ZoneId": 100006
            },
            {
                "ClusterId": 0,
                "NodeId": "78dd8883679ecda91293ded3051db82eec220da3",
                "NodeRole": "master",
                "ZoneId": 100006
            },
            {
                "ClusterId": 0,
                "NodeId": "134940b760fcfa727cc030b5a5e622e88b00af5c",
                "NodeRole": "slave",
                "ZoneId": 100004
            },
            {
                "ClusterId": 0,
                "NodeId": "58b509ea080e53d5aa71776688d2b70b23c63341",
                "NodeRole": "slave",
                "ZoneId": 100006
            },
            {
                "ClusterId": 0,
                "NodeId": "b451eafdfe3fa6fcd2f309b3a874414e255fc7e9",
                "NodeRole": "slave",
                "ZoneId": 100006
            },
            {
                "ClusterId": 0,
                "NodeId": "eb7baf3b620417f2ac7b2e61db47494bfe944a20",
                "NodeRole": "slave",
                "ZoneId": 100006
            },
            {
                "ClusterId": 0,
                "NodeId": "1f4fc3cf0f5dd641896fab7346c19486854b91cf",
                "NodeRole": "slave",
                "ZoneId": 100006
            },
            {
                "ClusterId": 0,
                "NodeId": "365e4bd53d1b22b7b11a478e59bedd7b36664168",
                "NodeRole": "slave",
                "ZoneId": 100004
            },
            {
                "ClusterId": 0,
                "NodeId": "6906d69a5378dc368da4cc3b0a924608ded3033a",
                "NodeRole": "slave",
                "ZoneId": 100006
            },
            {
                "ClusterId": 0,
                "NodeId": "7bf8f6080c14b449a617cff4ad4fd2b326198314",
                "NodeRole": "slave",
                "ZoneId": 100006
            },
            {
                "ClusterId": 0,
                "NodeId": "14f01a4ae7aa67aa163494bbc6e8c084961b3ca2",
                "NodeRole": "slave",
                "ZoneId": 100004
            },
            {
                "ClusterId": 0,
                "NodeId": "165bc741b8f9e929b382a6ea14ce8e9d243b4ad9",
                "NodeRole": "slave",
                "ZoneId": 100006
            },
            {
                "ClusterId": 0,
                "NodeId": "aaafa08a670047eaed7662b09ddac78e2a449590",
                "NodeRole": "slave",
                "ZoneId": 100006
            },
            {
                "ClusterId": 0,
                "NodeId": "cc37908d0829a977727ebccbac393e1e6eacb7b6",
                "NodeRole": "slave",
                "ZoneId": 100006
            }
        ],
        "RedisCount": 15,
        "RequestId": "eba33751-49d1-43a8-a4c5-5a3596b41f06",
        "Tendis": [],
        "TendisCount": 0
    }
}
```


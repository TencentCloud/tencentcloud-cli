**Example 1: 创建HTTPS监听器，并绑定已有证书**

创建HTTPS监听器，并绑定已有证书

Input: 

```
tccli clb CreateListener --cli-unfold-argument  \
    --Protocol HTTPS \
    --Ports 7572 \
    --Certificate.SSLMode UNIDIRECTIONAL \
    --Certificate.CertId MsJyaXVm \
    --LoadBalancerId lb-cuxw2rm0
```

Output: 
```
{
    "Response": {
        "ListenerIds": [
            "lbl-4fbxq45k"
        ],
        "RequestId": "db8ae69f-ebda-402b-8d02-ead459aa6ff9"
    }
}
```

**Example 2: 创建TCP监听器的同时设置健康检查信息**

创建TCP监听器的同时设置健康检查信息

Input: 

```
tccli clb CreateListener --cli-unfold-argument  \
    --HealthCheck.UnHealthNum 4 \
    --HealthCheck.HealthNum 4 \
    --HealthCheck.IntervalTime 7 \
    --HealthCheck.TimeOut 5 \
    --HealthCheck.HealthSwitch 1 \
    --Protocol TCP \
    --Ports 7571 \
    --LoadBalancerId lb-cuxw2rm0
```

Output: 
```
{
    "Response": {
        "ListenerIds": [
            "lbl-lbbxvq26"
        ],
        "RequestId": "fff13c83-dcb5-481a-ba7c-30e92c276c19"
    }
}
```

**Example 3: 创建HTTPS监听器，并同时绑定新建的证书**

创建HTTPS监听器，并同时绑定新建的证书

Input: 

```
tccli clb CreateListener --cli-unfold-argument  \
    --Protocol HTTPS \
    --Ports 7573 \
    --Certificate.SSLMode UNIDIRECTIONAL \
    --Certificate.CertContent -----BEGINCERTIFICATE-----\nxxxxxxxxxxxxxxxxxxxxxxx\n-----ENDCERTIFICATE----- \
    --Certificate.CertName my-cert \
    --Certificate.CertKey -----BEGINRSAPRIVATEKEY-----\nxxxxxxxxxxxxxxxxxxxxxxxx\n-----ENDRSAPRIVATEKEY----- \
    --LoadBalancerId lb-cuxw2rm0
```

Output: 
```
{
    "Response": {
        "ListenerIds": [
            "lbl-bzfmg9m6"
        ],
        "RequestId": "6082314c-030c-429d-9eae-2dc6b159b5b9"
    }
}
```

**Example 4: 创建UDP监听器，健康检查方式使用Ping（默认方式）**

创建UDP监听器，健康检查方式使用Ping（默认方式）

Input: 

```
tccli clb CreateListener --cli-unfold-argument  \
    --HealthCheck.HealthSwitch 1 \
    --Protocol UDP \
    --ListenerNames lis_test \
    --Ports 432 \
    --LoadBalancerId lb-6wlxe9rj
```

Output: 
```
{
    "Response": {
        "ListenerIds": [
            "lbl-aev333n1"
        ],
        "RequestId": "3b81f03e-6088-448d-abaf-8a487d4f985a"
    }
}
```

**Example 5: 创建两个TCP监听器，分别监听7569和7570端口，并分别命名为lis0和lis1**

创建两个TCP监听器，分别监听7569和7570端口，并分别命名为lis0和lis1。

Input: 

```
tccli clb CreateListener --cli-unfold-argument  \
    --ListenerNames lis1 lis0 \
    --Protocol TCP \
    --Ports 7570 7569 \
    --LoadBalancerId lb-cuxw2rm0
```

Output: 
```
{
    "Response": {
        "ListenerIds": [
            "lbl-d1ubsydq",
            "lbl-4udz130k"
        ],
        "RequestId": "8f272cef-14ff-458c-b67e-1bd21bd2942b"
    }
}
```

**Example 6: 创建监听器，开启重新调度功能**



Input: 

```
tccli clb CreateListener --cli-unfold-argument  \
    --LoadBalancerId lb-fd9kpk4s \
    --Ports 5689 \
    --Protocol tcp \
    --RescheduleTargetZeroWeight True \
    --RescheduleUnhealthy True \
    --RescheduleExpandTarget True \
    --RescheduleStartTime 25 \
    --RescheduleInterval 50
```

Output: 
```
{
    "Response": {
        "ListenerIds": [
            "lbl-1sf4yxie"
        ],
        "RequestId": "6aa274e5-ff78-4e9e-b13c-30a9e21b107e"
    }
}
```


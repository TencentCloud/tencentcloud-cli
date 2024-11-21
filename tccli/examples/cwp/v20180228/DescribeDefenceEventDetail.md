**Example 1: 获取漏洞防御事件详情**



Input: 

```
tccli cwp DescribeDefenceEventDetail --cli-unfold-argument  \
    --Id 13844
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 13844,
            "Status": 1,
            "Quuid": "acdd5474-6360-4fd4-bfc7-843162cb8116",
            "Alias": "machinename",
            "MachineStatus": "ONLINE",
            "PrivateIp": "10.0.1.233",
            "PublicIp": "43.138.142.208",
            "CreateTime": "2024-11-03 00:40:12",
            "MergeTime": "2024-11-03 16:25:04",
            "VulName": "ISC BIND 资源管理错误漏洞(CVE-2014-8500)",
            "EventType": 2,
            "Count": 76,
            "CveId": "CVE-2014-8500",
            "SourceIp": "na",
            "City": "gz",
            "SourcePort": [
                80
            ],
            "Description": "ISCBIND是美国InternetSystemsConsortium（ISC）公司所维护的一套实现了DNS协议的开源软件。ISCBIND中存在安全漏洞，该漏洞源于程序没有限制授权链。远程攻击者可利用该漏洞造成拒绝服务（内存消耗）。以下版本受到影响：ISCBIND9.0.x至9.8.x版本，9.9.0至9.9.6版本，9.10.0至9.10.1版本。",
            "Fix": "建议您更新当前系统或软件至最新版，完成漏洞的修复。",
            "NetworkPayload": "bnVsbDogZXhhbXBsZS5jb20vCm51bGxAI0Bob3N0OiBleGFtcGxlLmNvbQp1c2VyLWFnZW50OiBHby1odHRwLWNsaWVudC8xLjEKYWNjZXB0LWVuY29kaW5nOiBnemlwCmNvbm5lY3Rpb246IGNsb3NlCg==",
            "Pid": 3380048,
            "MainClass": "org.apache.catalina.startup.Bootstrap",
            "StackTrace": "org.apache.catalina.core.ApplicationFilterChain.doFilter\norg.apache.catalina.core.StandardWrapperValve.invoke\norg.apache.catalina.core.StandardContextValve.invoke\norg.apache.catalina.authenticator.AuthenticatorBase.invoke\norg.apache.catalina.core.StandardHostValve.invoke\norg.apache.catalina.valves.ErrorReportValve.invoke\norg.apache.catalina.valves.AbstractAccessLogValve.invoke\norg.apache.catalina.core.StandardEngineValve.invoke\norg.apache.catalina.connector.CoyoteAdapter.service\norg.apache.coyote.http11.Http11Processor.service\norg.apache.coyote.AbstractProcessorLight.process\norg.apache.coyote.AbstractProtocol$ConnectionHandler.process\norg.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun\norg.apache.tomcat.util.net.SocketProcessorBase.run\norg.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker\norg.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run\norg.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run\njava.lang.Thread.run\n",
            "EventDetail": "[{\"name\":\"hitSignatureID\",\"value\":\"14004\"},{\"name\":\"matches\",\"value\":\"example.com\"}]",
            "ExceptionPstree": "/bin/bash",
            "MachineExtraInfo": {
                "WanIP": "43.138.142.208",
                "PrivateIP": "10.0.1.233",
                "NetworkType": 1,
                "NetworkName": "vpc-mbgoxtov",
                "InstanceID": "ins-j7vumfb6",
                "HostName": "machinename"
            }
        },
        "RequestId": "6e91fa6a-9b0b-49d7-9ecd-679e5569b90e"
    }
}
```


**Example 1: 获取容器漏洞防御或者内存马注入告警详情**

获取容器漏洞防御或者内存马注入告警详情

Input: 

```
tccli cwp DescribeRaspEventDetailTCSS --cli-unfold-argument  \
    --Id 10010
```

Output: 
```
{
    "Response": {
        "Data": {
            "Alias": "",
            "AttackPort": 0,
            "AttackType": 0,
            "AttackTypeName": "",
            "City": "广东省-深圳市",
            "ClusterId": "",
            "ClusterName": "",
            "ContainerId": "645fa43394287c5fa81095a6ac29ce0382caadc6c2b541d7580fc14af0539c33",
            "ContainerName": "/gracious_saha",
            "ContainerNetStatus": "",
            "ContainerStatus": "",
            "Count": 3,
            "CreateTime": "2022-07-25 16:20:49",
            "CveId": "CVE-2021-44832",
            "Description": "Apache Log4j2 发布安全通告，2.17.1之前的版本容易受到远程代码执行攻击，当攻击者有权限修改日志配置的情况下，可远程执行代码。",
            "Fix": "请注意，该漏洞仅对log4j-core文件版本做检测，默认配置的情况下，仍然会检出；\n\n只有 log4j-core JAR 文件受此漏洞影响。仅使用 log4j-api JAR 文件而不使用 log4j-core JAR 文件的应用程序不受此漏洞的影响。腾讯安全专家建议受影响的用户尽快升级到2.17.1及以上版本。\n最新安全版本请参考官方安全通告：https://logging.apache.org/log4j/2.x/security.html\n更新包下载地址：https://logging.apache.org/log4j/2.x/download.html",
            "HostTags": [],
            "Id": 0,
            "ImageId": "sha256:d76d5658637ff855abdfda4d66eaa4c8f765eb9299456d984c8050e0974208f2",
            "ImageName": "tomcat7:jdk8",
            "InstanceID": "",
            "MainClass": "org.apache.catalina.startup.Bootstrap",
            "MergeTime": "2022-07-25 16:27:53",
            "NetworkPayload": "aG9zdDoxMDYuNTIuMjkuMTMzOjg4ODgKY29ubmVjdGlvbjprZWVwLWFsaXZlCmNvbnRlbnQtbGVuZ3RoOjcwCmNhY2hlLWNvbnRyb2w6bWF4LWFnZT0wCnVwZ3JhZGUtaW5zZWN1cmUtcmVxdWVzdHM6MQpvcmlnaW46aHR0cDovLzEwNi41Mi4yOS4xMzM6ODg4OApjb250ZW50LXR5cGU6YXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkCnVzZXItYWdlbnQ6TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjAuMCBTYWZhcmkvNTM3LjM2CmFjY2VwdDp0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS9hdmlmLGltYWdlL3dlYnAsaW1hZ2UvYXBuZywqLyo7cT0wLjgsYXBwbGljYXRpb24vc2lnbmVkLWV4Y2hhbmdlO3Y9YjM7cT0wLjkKcmVmZXJlcjpodHRwOi8vMTA2LjUyLjI5LjEzMzo4ODg4L2xvZzRqLwphY2NlcHQtZW5jb2Rpbmc6Z3ppcCwgZGVmbGF0ZQphY2NlcHQtbGFuZ3VhZ2U6emgtQ04semg7cT0wLjksZW47cT0wLjgKY29va2llOkpTRVNTSU9OSUQ9N0Y5OTc4NkVENDc3RUU4MTEwODlBOEVCMTMwQjExRkY7IEpTRVNTSU9OSUQ9NDkzQUY0QzE4QjYxOTQ0NTEzNDMyOEEwMEVFREQ5RjYK",
            "NodeId": "",
            "NodeName": "",
            "Pid": 240223,
            "PodIp": "",
            "PodName": "",
            "PrivateIp": "",
            "PublicIp": "",
            "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
            "RaspDetail": "[{\"name\":\"jndiurl\",\"value\":\"ldap://m1111cak1z.dnslog.cn/\"}]",
            "SourceIp": "113.108.77.67",
            "StackTrace": "org.apache.logging.log4j.core.net.JndiManager.lookup\norg.apache.logging.log4j.core.lookup.JndiLookup.lookup\norg.apache.logging.log4j.core.lookup.Interpolator.lookup\norg.apache.logging.log4j.core.lookup.StrSubstitutor.resolveVariable\norg.apache.logging.log4j.core.lookup.StrSubstitutor.substitute\norg.apache.logging.log4j.core.lookup.StrSubstitutor.substitute\norg.apache.logging.log4j.core.lookup.StrSubstitutor.replace\norg.apache.logging.log4j.core.pattern.MessagePatternConverter.format\norg.apache.logging.log4j.core.pattern.PatternFormatter.format\norg.apache.logging.log4j.core.layout.PatternLayout.toSerializable\norg.apache.logging.log4j.core.layout.PatternLayout.toSerializable\norg.apache.logging.log4j.core.layout.AbstractStringLayout.toByteArray\norg.apache.logging.log4j.core.appender.AbstractOutputStreamAppender.append\norg.apache.logging.log4j.core.config.AppenderControl.callAppender\norg.apache.logging.log4j.core.config.LoggerConfig.callAppenders\norg.apache.logging.log4j.core.config.LoggerConfig.log\norg.apache.logging.log4j.core.config.LoggerConfig.log\norg.apache.logging.log4j.core.Logger.logMessage\norg.apache.logging.log4j.spi.AbstractLogger.logMessage\norg.apache.logging.log4j.spi.AbstractLogger.logIfEnabled\norg.apache.logging.log4j.spi.AbstractLogger.error\ncom.ki.demo2.BaseServlet.doPost\njavax.servlet.http.HttpServlet.service\njavax.servlet.http.HttpServlet.service\norg.apache.catalina.core.ApplicationFilterChain.internalDoFilter\norg.apache.catalina.core.ApplicationFilterChain.doFilter\norg.apache.catalina.core.StandardWrapperValve.invoke\norg.apache.catalina.core.StandardContextValve.invoke\norg.apache.catalina.authenticator.AuthenticatorBase.invoke\norg.apache.catalina.core.StandardHostValve.invoke\norg.apache.catalina.valves.ErrorReportValve.invoke\norg.apache.catalina.valves.AccessLogValve.invoke\norg.apache.catalina.core.StandardEngineValve.invoke\norg.apache.catalina.connector.CoyoteAdapter.service\norg.apache.coyote.http11.AbstractHttp11Processor.process\norg.apache.coyote.AbstractProtocol$AbstractConnectionHandler.process\norg.apache.tomcat.util.net.JIoEndpoint$SocketProcessor.run\njava.util.concurrent.ThreadPoolExecutor.runWorker\njava.util.concurrent.ThreadPoolExecutor$Worker.run\njava.lang.Thread.run\n",
            "Status": 0,
            "Url": "",
            "VulName": "Apache log4j2 远程代码执行漏洞 (CVE-2021-44832)"
        },
        "RequestId": "b38481d0-106b-49d8-8069-19be9a2f4425"
    }
}
```


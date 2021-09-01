**Example 1: 标准输出日志搜索**



Input: 

```
tccli tsf SearchStdoutLog --cli-unfold-argument  \
    --Limit 100 \
    --StartTime '2019-05-29 14:14:42' \
    --InstanceId msjw-uniform-payment-5ffb678dbf-mctr7
```

Output: 
```
{
    "Response": {
        "RequestId": "273aa44b-85d2-4279-9840-91b742eed7d0",
        "Result": {
            "TotalCount": 165,
            "Content": [
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.933][main] INFO  o.s.b.c.e.t.TomcatEmbeddedServletContainer - Tomcat started on port(s): 8080 (http)",
                    "Timestamp": 1559114131428
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.947][main] INFO  o.s.c.c.s.ConsulServiceRegistry - Registering service with consul: TsfNewService{id='msjw-uniform-payment-5ffb678dbf-mctr7', name='msjw-uniform-payment', tags=[contextPath=/msjwUniformPay], address='172.16.0.93', port=8080, meta={TSF_INSTNACE_ID=msjw-uniform-payment-5ffb678dbf-mctr7, TSF_PROG_VERSION=20190528175713, TSF_GROUP_ID=group-py5479ja, TSF_API_METAS=H4sIAAAAAAAAAO1bS3PbNhD+Kxq2R8pynEwPvjmKM+OJI2ssuzl0eoDIlYiEBBgAtKpm9Iv6E3rLL+sC1IMPgHrGqRLN+CJ+i8Vi8",
                    "Timestamp": 1559114131428
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:28.061][main] INFO  cn.gov.szga.Application - Started Application in 12.068 seconds (JVM running for 12.71)",
                    "Timestamp": 1559114131428
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:26.641][elasticsearch[Achilles][clusterService#updateTask][T#1]] INFO  org.elasticsearch.gateway - [Achilles] recovered [0] indices into cluster_state",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.044][main] INFO  c.n.c.sources.URLConfigurationSource - URLs to be used as dynamic configuration source: [jar:file:/data/tsf_default/msjw-uniform-payment.jar!/BOOT-INF/classes!/config.properties]",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.247][main] INFO  o.s.j.e.a.AnnotationMBeanExporter - Registering beans for JMX exposure on startup",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.468][main] INFO  o.s.c.s.DefaultLifecycleProcessor - Starting beans in phase -3",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.468][main] INFO  s.d.s.w.p.DocumentationPluginsBootstrapper - Context refreshed",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.486][main] INFO  s.d.s.w.p.DocumentationPluginsBootstrapper - Found 1 custom documentation plugin(s)",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.525][main] INFO  s.d.s.w.s.ApiListingReferenceScanner - Scanning for api listing references",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.741][main] INFO  o.s.c.s.DefaultLifecycleProcessor - Starting beans in phase -2",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.896][main] INFO  o.a.coyote.http11.Http11NioProtocol - Starting ProtocolHandler [\"http-nio-8080\"]",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:26.522][elasticsearch[Achilles][clusterService#updateTask][T#1]] INFO  org.elasticsearch.cluster.service - [Achilles] new_master {Achilles}{XE4pHz4UQkmc4B-UaRzRtg}{local}{local[1]}{local=true}, reason: local-disco-initial_connect(master)",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:26.529][main] INFO  org.elasticsearch.node - [Achilles] started",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.026][main] INFO  c.n.c.sources.URLConfigurationSource - URLs to be used as dynamic configuration source: [jar:file:/data/tsf_default/msjw-uniform-payment.jar!/BOOT-INF/classes!/config.properties]",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.249][main] INFO  o.s.j.e.a.AnnotationMBeanExporter - Bean with name 'dataSource' has been autodetected for JMX exposure",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.259][main] INFO  o.s.j.e.a.AnnotationMBeanExporter - Bean with name 'refreshScope' has been autodetected for JMX exposure",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.262][main] INFO  o.s.j.e.a.AnnotationMBeanExporter - Located managed bean 'environmentManager': registering with JMX server as MBean [org.springframework.cloud.context.environment:name=environmentManager,type=EnvironmentManager]",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.275][main] INFO  o.s.j.e.a.AnnotationMBeanExporter - Located managed bean 'refreshScope': registering with JMX server as MBean [org.springframework.cloud.context.scope.refresh:name=refreshScope,type=RefreshScope]",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.885][main] INFO  o.s.c.s.DefaultLifecycleProcessor - Starting beans in phase 0",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.904][main] INFO  o.a.tomcat.util.net.NioSelectorPool - Using a shared selector for servlet write/read",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:26.513][main] INFO  org.elasticsearch.discovery - [Achilles] elasticsearch/XE4pHz4UQkmc4B-UaRzRtg",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.258][main] INFO  o.s.j.e.a.AnnotationMBeanExporter - Bean with name 'configurationPropertiesRebinder' has been autodetected for JMX exposure",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.259][main] INFO  o.s.j.e.a.AnnotationMBeanExporter - Bean with name 'environmentManager' has been autodetected for JMX exposure",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.288][main] INFO  o.s.j.e.a.AnnotationMBeanExporter - Located managed bean 'configurationPropertiesRebinder': registering with JMX server as MBean [org.springframework.cloud.context.properties:name=configurationPropertiesRebinder,context=2b2948e2,type=ConfigurationPropertiesRebinder]",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.294][main] INFO  o.s.j.e.a.AnnotationMBeanExporter - Located MBean 'dataSource': registering with JMX server as MBean [com.alibaba.druid.pool:name=dataSource,type=DruidDataSource]",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:27.885][main] INFO  o.s.c.s.DefaultLifecycleProcessor - Starting beans in phase -1",
                    "Timestamp": 1559114131427
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:22.608][main] INFO  o.s.w.s.m.m.a.RequestMappingHandlerMapping - Mapped \"{[/payNote/scheduler],methods=[POST],produces=[application/json]}\" onto public java.lang.String cn.gov.szga.uniform.payment.rest.PaymNoteScheduler.scheduler()",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:23.218][main] INFO  o.s.w.s.h.SimpleUrlHandlerMapping - Mapped URL path [/**/favicon.ico] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:24.174][main] INFO  org.elasticsearch.node - [Achilles] version[2.4.6], pid[15], build[5376dca/2017-07-18T12:17:44Z]",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:24.212][main] INFO  org.elasticsearch.env - [Achilles] using [1] data paths, mounts [[/ (none)]], net usable_space [171.5gb], net total_space [196.7gb], spins? [possibly], types [aufs]",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:24.213][main] INFO  org.elasticsearch.env - [Achilles] heap size [1.7gb], compressed ordinary object pointers [true]",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "OpenJDK 64-Bit Server VM warning: You have loaded library /tmp/jna2267817740774765773.tmp which might have disabled stack guard. The VM will try to fix the stack guard now.",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "It's highly recommended that you fix the library with 'execstack -c <libfile>', or link it with '-z noexecstack'.",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:26.507][main] INFO  org.elasticsearch.node - [Achilles] starting ...",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:22.613][main] INFO  o.s.w.s.m.m.a.RequestMappingHandlerMapping - Mapped \"{[/swagger-resources/configuration/security]}\" onto public org.springframework.http.ResponseEntity<springfox.documentation.swagger.web.SecurityConfiguration> springfox.documentation.swagger.web.ApiResourceController.securityConfiguration()",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:23.089][main] INFO  o.s.w.s.m.m.a.RequestMappingHandlerAdapter - Looking for @ControllerAdvice: org.springframework.boot.context.embedded.AnnotationConfigEmbeddedWebApplicationContext@2b2948e2: startup date [Wed May 29 15:15:17 CST 2019]; parent: org.springframework.context.annotation.AnnotationConfigApplicationContext@dcf3e99",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:23.162][main] INFO  o.s.w.s.h.SimpleUrlHandlerMapping - Mapped URL path [/webjars/**] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:23.882][main] INFO  s.d.s.w.PropertySourcedRequestMappingHandlerMapping - Mapped URL path [/v2/api-docs] onto method [public org.springframework.http.ResponseEntity<springfox.documentation.spring.web.json.Json> springfox.documentation.swagger2.web.Swagger2Controller.getDocumentation(java.lang.String,javax.servlet.http.HttpServletRequest)]",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:26.510][main] INFO  org.elasticsearch.transport - [Achilles] publish_address {local[1]}, bound_addresses {local[1]}",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:22.613][main] INFO  o.s.w.s.m.m.a.RequestMappingHandlerMapping - Mapped \"{[/swagger-resources]}\" onto public org.springframework.http.ResponseEntity<java.util.List<springfox.documentation.swagger.web.SwaggerResource>> springfox.documentation.swagger.web.ApiResourceController.swaggerResources()",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:22.614][main] INFO  o.s.w.s.m.m.a.RequestMappingHandlerMapping - Mapped \"{[/swagger-resources/configuration/ui]}\" onto public org.springframework.http.ResponseEntity<springfox.documentation.swagger.web.UiConfiguration> springfox.documentation.swagger.web.ApiResourceController.uiConfiguration()",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:22.617][main] INFO  o.s.w.s.m.m.a.RequestMappingHandlerMapping - Mapped \"{[/error],produces=[text/html]}\" onto public org.springframework.web.servlet.ModelAndView org.springframework.boot.autoconfigure.web.BasicErrorController.errorHtml(javax.servlet.http.HttpServletRequest,javax.servlet.http.HttpServletResponse)",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:22.617][main] INFO  o.s.w.s.m.m.a.RequestMappingHandlerMapping - Mapped \"{[/error]}\" onto public org.springframework.http.ResponseEntity<java.util.Map<java.lang.String, java.lang.Object>> org.springframework.boot.autoconfigure.web.BasicErrorController.error(javax.servlet.http.HttpServletRequest)",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:23.162][main] INFO  o.s.w.s.h.SimpleUrlHandlerMapping - Mapped URL path [/**] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:23.906][main] INFO  c.t.t.s.a.TsfSwaggerAutoConfiguration - [tsf-swagger] application main class:cn.gov.szga.Application, auto detect swagger scan package:cn.gov.szga ",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:24.174][main] INFO  org.elasticsearch.node - [Achilles] initializing ...",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:24.180][main] INFO  org.elasticsearch.plugins - [Achilles] modules [], plugins [], sites []",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:26.507][main] INFO  org.elasticsearch.node - [Achilles] initialized",
                    "Timestamp": 1559114131426
                },
                {
                    "InstanceId": "msjw-uniform-payment-5ffb678dbf-mctr7",
                    "InstanceIp": "172.16.0.93",
                    "Content": "[2019/05/29 15:15:21.762][localhost-startStop-1] INFO  o.s.b.w.s.FilterRegistrationBean - Mapping filter: 'requestContextFilter' to: [/*]",
                    "Timestamp": 1559114131425
                }
            ]
        }
    }
}
```


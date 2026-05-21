**Example 1: Labels值查询**

```
Path: /api/v1/label/<label_name>/values
Method: GET
Query参数: 
   1. match[] = <series_selector> prometheus查询表达式，返回匹配的时间线
   2. start = <rfc3339 | unix_timestamp> 查询起始时间
   3. end = <rfc3339 | unix_timestamp> 查询结束时间 (结束时间要晚于起始时间)
响应体:
{
	"status": "success" | "error",
	"data": [
		// match[] 匹配到的key为label_name的所有值
		"value1",
		"value2"
		// ...
	],
	
	// 错误时返回
	"errorType": "<string>",
	"error": "<string>",

	// warning 信息
	"warnings": ["<string>"]
}
```

Input: 

```
tccli monitor RoutePrometheusDynamicAPI --cli-unfold-argument  \
    --InstanceId prom-xz223asd \
    --Method GET \
    --Path /api/v1/label/__name__/values?match[]=up&match[]=ALERTS{}
```

Output: 
```
{
    "Response": {
        "HTTP": {
            "StatusCode": 200,
            "ResponseBody": "{\"status\":\"success\",\"data\":[\"ALERTS\",\"up\"]}"
        },
        "RequestId": "3q393dqikzp-mebz4bi9xsta9zzb7q54"
    }
}
```

**Example 2: Labels查询**

```
Path: /api/v1/labels
Method: GET POST
Query参数: 
   1. match[] = <series_selector> prometheus查询表达式，返回匹配的时间线
   2. start = <rfc3339 | unix_timestamp> 查询起始时间
   3. end = <rfc3339 | unix_timestamp> 查询结束时间 (结束时间要晚于起始时间)
响应体:
{
	"status": "success" | "error",
	"data": [
		// match[] 匹配到的所有label name
		"__name__",
		"job"
		// ...
	],
	
	// 错误时返回
	"errorType": "<string>",
	"error": "<string>",

	// warning 信息
	"warnings": ["<string>"]
}
```

Input: 

```
tccli monitor RoutePrometheusDynamicAPI --cli-unfold-argument  \
    --InstanceId prom-xz223asd \
    --Method POST \
    --Path /api/v1/labels?match[]=up&match[]=ALERTS{}
```

Output: 
```
{
    "Response": {
        "HTTP": {
            "StatusCode": 200,
            "ResponseBody": "{\"status\":\"success\",\"data\":[\"__name__\",\"_appid_\",\"_instanceid_\",\"_interval_\",\"_language_\",\"_policyid_\",\"_policyname_\",\"_region_\",\"_regionid_\",\"_subaccountuin_\",\"_uin_\",\"alertName\",\"alertname\",\"alertstate\",\"beta_kubernetes_io_arch\",\"beta_kubernetes_io_instance_type\",\"beta_kubernetes_io_os\",\"c\",\"cloud_tencent_com_node_instance_id\",\"cluster\",\"cluster_type\",\"container\",\"endpoint\",\"failure_domain_beta_kubernetes_io_region\",\"failure_domain_beta_kubernetes_io_zone\",\"instance\",\"job\",\"kubernetes_io_arch\",\"kubernetes_io_hostname\",\"kubernetes_io_os\",\"namespace\",\"node\",\"node_kubernetes_io_instance_type\",\"notification\",\"notify_way\",\"pod\",\"service\",\"severity\",\"tcloud_region_id\",\"tcloud_region_name\",\"tke_cloud_tencent_com_cbs_mountable\",\"tke_scene_flag\",\"topology_com_tencent_cloud_csi_cbs_zone\",\"topology_kubernetes_io_region\",\"topology_kubernetes_io_zone\"]}"
        },
        "RequestId": "92rmr4l74y37llzqc2nz-mn8usc93qq-"
    }
}
```

**Example 3: 时间线查询 GET**

```
Path: /api/v1/series
Method: GET POST
Query参数: 
   1. match[] = <series_selector> prometheus查询表达式，返回匹配的时间线
   2. start = <rfc3339 | unix_timestamp> 查询起始时间
   3. end = <rfc3339 | unix_timestamp> 查询结束时间 (结束时间要晚于起始时间)
响应体:
{
	"status": "success" | "error",
	"data": [
		{
			"__name__": <string>,
			// series labels ...,
			"job": "xxx",
			"instance": "xxx"
		}
	],
	
	// 错误时返回
	"errorType": "<string>",
	"error": "<string>",

	// warning 信息
	"warnings": ["<string>"]
}
```

Input: 

```
tccli monitor RoutePrometheusDynamicAPI --cli-unfold-argument  \
    --InstanceId prom-xz223asd \
    --Method GET \
    --Path /api/v1/series?match[]=up&match[]=ALERTS{}
```

Output: 
```
{
    "Response": {
        "HTTP": {
            "StatusCode": 200,
            "ResponseBody": "{\"status\":\"success\",\"data\":[{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_interval_\":\"5m\",\"_language_\":\"zh-CN\",\"_policyid_\":\"arule-2wou7mfi\",\"_policyname_\":\"test-monitor-alert\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"100026263254\",\"_uin_\":\"1500000688\",\"alertname\":\"test-monitor-alert\",\"alertstate\":\"firing\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_language_\":\"zh-CN\",\"_policyname_\":\"al-test-changed/aaaaa\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"100026263254\",\"_uin_\":\"1500000688\",\"alertname\":\"al-test-changed/aaaaa\",\"alertstate\":\"firing\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_language_\":\"zh-CN\",\"_policyname_\":\"alertgroup-in-tke/alert-1\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"4611686018429437801\",\"_uin_\":\"1500000688\",\"alertname\":\"alertgroup-in-tke/alert-1\",\"alertstate\":\"firing\",\"severity\":\"warning\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_language_\":\"zh-CN\",\"_policyname_\":\"alertgroup-in-tke/alert-2\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"4611686018429437801\",\"_uin_\":\"1500000688\",\"alertname\":\"alertgroup-in-tke/alert-2\",\"alertstate\":\"firing\",\"severity\":\"warning\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},{\"__name__\":\"up\",\"beta_kubernetes_io_arch\":\"amd64\",\"beta_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"beta_kubernetes_io_os\":\"linux\",\"cloud_tencent_com_node_instance_id\":\"ins-iw1k7u0g\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"failure_domain_beta_kubernetes_io_region\":\"cq\",\"failure_domain_beta_kubernetes_io_zone\":\"190001\",\"instance\":\"10.0.0.196\",\"job\":\"cadvisor\",\"kubernetes_io_arch\":\"amd64\",\"kubernetes_io_hostname\":\"10.0.0.196\",\"kubernetes_io_os\":\"linux\",\"node_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_cloud_tencent_com_cbs_mountable\":\"true\",\"tke_scene_flag\":\"true\",\"topology_com_tencent_cloud_csi_cbs_zone\":\"ap-chongqing-1\",\"topology_kubernetes_io_region\":\"cq\",\"topology_kubernetes_io_zone\":\"190001\"},{\"__name__\":\"up\",\"beta_kubernetes_io_arch\":\"amd64\",\"beta_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"beta_kubernetes_io_os\":\"linux\",\"cloud_tencent_com_node_instance_id\":\"ins-iw1k7u0g\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"failure_domain_beta_kubernetes_io_region\":\"cq\",\"failure_domain_beta_kubernetes_io_zone\":\"190001\",\"instance\":\"10.0.0.196\",\"job\":\"kubelet\",\"kubernetes_io_arch\":\"amd64\",\"kubernetes_io_hostname\":\"10.0.0.196\",\"kubernetes_io_os\":\"linux\",\"node_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_cloud_tencent_com_cbs_mountable\":\"true\",\"tke_scene_flag\":\"true\",\"topology_com_tencent_cloud_csi_cbs_zone\":\"ap-chongqing-1\",\"topology_kubernetes_io_region\":\"cq\",\"topology_kubernetes_io_zone\":\"190001\"},{\"__name__\":\"up\",\"beta_kubernetes_io_arch\":\"amd64\",\"beta_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"beta_kubernetes_io_os\":\"linux\",\"cloud_tencent_com_node_instance_id\":\"ins-ka1tk14k\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"failure_domain_beta_kubernetes_io_region\":\"cq\",\"failure_domain_beta_kubernetes_io_zone\":\"190001\",\"instance\":\"10.0.0.185\",\"job\":\"cadvisor\",\"kubernetes_io_arch\":\"amd64\",\"kubernetes_io_hostname\":\"10.0.0.185\",\"kubernetes_io_os\":\"linux\",\"node_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_cloud_tencent_com_cbs_mountable\":\"true\",\"tke_scene_flag\":\"true\",\"topology_com_tencent_cloud_csi_cbs_zone\":\"ap-chongqing-1\",\"topology_kubernetes_io_region\":\"cq\",\"topology_kubernetes_io_zone\":\"190001\"},{\"__name__\":\"up\",\"beta_kubernetes_io_arch\":\"amd64\",\"beta_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"beta_kubernetes_io_os\":\"linux\",\"cloud_tencent_com_node_instance_id\":\"ins-ka1tk14k\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"failure_domain_beta_kubernetes_io_region\":\"cq\",\"failure_domain_beta_kubernetes_io_zone\":\"190001\",\"instance\":\"10.0.0.185\",\"job\":\"kubelet\",\"kubernetes_io_arch\":\"amd64\",\"kubernetes_io_hostname\":\"10.0.0.185\",\"kubernetes_io_os\":\"linux\",\"node_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_cloud_tencent_com_cbs_mountable\":\"true\",\"tke_scene_flag\":\"true\",\"topology_com_tencent_cloud_csi_cbs_zone\":\"ap-chongqing-1\",\"topology_kubernetes_io_region\":\"cq\",\"topology_kubernetes_io_zone\":\"190001\"},{\"__name__\":\"up\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"container\":\"kube-state-metrics\",\"endpoint\":\"http-metrics\",\"instance\":\"172.19.0.23:8180\",\"job\":\"kube-state-metrics\",\"namespace\":\"kube-system\",\"pod\":\"tke-kube-state-metrics-0\",\"service\":\"tke-kube-state-metrics\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_scene_flag\":\"true\"},{\"__name__\":\"up\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"container\":\"node-exporter\",\"instance\":\"10.0.0.185\",\"job\":\"node-exporter\",\"namespace\":\"kube-system\",\"pod\":\"tke-node-exporter-rltlc\",\"service\":\"tke-node-exporter\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_scene_flag\":\"true\"},{\"__name__\":\"up\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"container\":\"node-exporter\",\"instance\":\"10.0.0.196\",\"job\":\"node-exporter\",\"namespace\":\"kube-system\",\"pod\":\"tke-node-exporter-4lcms\",\"service\":\"tke-node-exporter\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_scene_flag\":\"true\"},{\"__name__\":\"up\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"instance\":\"10.0.0.3:9091\",\"job\":\"job1\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_scene_flag\":\"true\"},{\"__name__\":\"up\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"instance\":\"10.0.0.3:9091\",\"job\":\"job2\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_scene_flag\":\"true\"}]}"
        },
        "RequestId": "g1sa-v1z--ebeavewsaenpmt8igv7trm"
    }
}
```

**Example 4: 时间线查询 POST**

同时间线查询GET

在match[]参数过长时可以通过`Content-Type: application/x-www-form-urlencoded`，将查询参数放在请求体

Input: 

```
tccli monitor RoutePrometheusDynamicAPI --cli-unfold-argument  \
    --InstanceId prom-xz223asd \
    --Method POST \
    --Path /api/v1/series \
    --Headers.0.Key Content-Type \
    --Headers.0.Value application/x-www-form-urlencoded \
    --RequestBody match[]=up&match[]=ALERTS{}
```

Output: 
```
{
    "Response": {
        "HTTP": {
            "StatusCode": 200,
            "ResponseBody": "{\"status\":\"success\",\"data\":[{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_interval_\":\"5m\",\"_language_\":\"zh-CN\",\"_policyid_\":\"arule-2wou7mfi\",\"_policyname_\":\"test-monitor-alert\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"100026263254\",\"_uin_\":\"1500000688\",\"alertname\":\"test-monitor-alert\",\"alertstate\":\"firing\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_language_\":\"zh-CN\",\"_policyname_\":\"al-test-changed/aaaaa\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"100026263254\",\"_uin_\":\"1500000688\",\"alertname\":\"al-test-changed/aaaaa\",\"alertstate\":\"firing\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_language_\":\"zh-CN\",\"_policyname_\":\"alertgroup-in-tke/alert-1\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"4611686018429437801\",\"_uin_\":\"1500000688\",\"alertname\":\"alertgroup-in-tke/alert-1\",\"alertstate\":\"firing\",\"severity\":\"warning\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_language_\":\"zh-CN\",\"_policyname_\":\"alertgroup-in-tke/alert-2\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"4611686018429437801\",\"_uin_\":\"1500000688\",\"alertname\":\"alertgroup-in-tke/alert-2\",\"alertstate\":\"firing\",\"severity\":\"warning\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},{\"__name__\":\"up\",\"beta_kubernetes_io_arch\":\"amd64\",\"beta_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"beta_kubernetes_io_os\":\"linux\",\"cloud_tencent_com_node_instance_id\":\"ins-iw1k7u0g\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"failure_domain_beta_kubernetes_io_region\":\"cq\",\"failure_domain_beta_kubernetes_io_zone\":\"190001\",\"instance\":\"10.0.0.196\",\"job\":\"cadvisor\",\"kubernetes_io_arch\":\"amd64\",\"kubernetes_io_hostname\":\"10.0.0.196\",\"kubernetes_io_os\":\"linux\",\"node_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_cloud_tencent_com_cbs_mountable\":\"true\",\"tke_scene_flag\":\"true\",\"topology_com_tencent_cloud_csi_cbs_zone\":\"ap-chongqing-1\",\"topology_kubernetes_io_region\":\"cq\",\"topology_kubernetes_io_zone\":\"190001\"},{\"__name__\":\"up\",\"beta_kubernetes_io_arch\":\"amd64\",\"beta_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"beta_kubernetes_io_os\":\"linux\",\"cloud_tencent_com_node_instance_id\":\"ins-iw1k7u0g\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"failure_domain_beta_kubernetes_io_region\":\"cq\",\"failure_domain_beta_kubernetes_io_zone\":\"190001\",\"instance\":\"10.0.0.196\",\"job\":\"kubelet\",\"kubernetes_io_arch\":\"amd64\",\"kubernetes_io_hostname\":\"10.0.0.196\",\"kubernetes_io_os\":\"linux\",\"node_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_cloud_tencent_com_cbs_mountable\":\"true\",\"tke_scene_flag\":\"true\",\"topology_com_tencent_cloud_csi_cbs_zone\":\"ap-chongqing-1\",\"topology_kubernetes_io_region\":\"cq\",\"topology_kubernetes_io_zone\":\"190001\"},{\"__name__\":\"up\",\"beta_kubernetes_io_arch\":\"amd64\",\"beta_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"beta_kubernetes_io_os\":\"linux\",\"cloud_tencent_com_node_instance_id\":\"ins-ka1tk14k\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"failure_domain_beta_kubernetes_io_region\":\"cq\",\"failure_domain_beta_kubernetes_io_zone\":\"190001\",\"instance\":\"10.0.0.185\",\"job\":\"cadvisor\",\"kubernetes_io_arch\":\"amd64\",\"kubernetes_io_hostname\":\"10.0.0.185\",\"kubernetes_io_os\":\"linux\",\"node_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_cloud_tencent_com_cbs_mountable\":\"true\",\"tke_scene_flag\":\"true\",\"topology_com_tencent_cloud_csi_cbs_zone\":\"ap-chongqing-1\",\"topology_kubernetes_io_region\":\"cq\",\"topology_kubernetes_io_zone\":\"190001\"},{\"__name__\":\"up\",\"beta_kubernetes_io_arch\":\"amd64\",\"beta_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"beta_kubernetes_io_os\":\"linux\",\"cloud_tencent_com_node_instance_id\":\"ins-ka1tk14k\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"failure_domain_beta_kubernetes_io_region\":\"cq\",\"failure_domain_beta_kubernetes_io_zone\":\"190001\",\"instance\":\"10.0.0.185\",\"job\":\"kubelet\",\"kubernetes_io_arch\":\"amd64\",\"kubernetes_io_hostname\":\"10.0.0.185\",\"kubernetes_io_os\":\"linux\",\"node_kubernetes_io_instance_type\":\"S5.MEDIUM4\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_cloud_tencent_com_cbs_mountable\":\"true\",\"tke_scene_flag\":\"true\",\"topology_com_tencent_cloud_csi_cbs_zone\":\"ap-chongqing-1\",\"topology_kubernetes_io_region\":\"cq\",\"topology_kubernetes_io_zone\":\"190001\"},{\"__name__\":\"up\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"container\":\"kube-state-metrics\",\"endpoint\":\"http-metrics\",\"instance\":\"172.19.0.23:8180\",\"job\":\"kube-state-metrics\",\"namespace\":\"kube-system\",\"pod\":\"tke-kube-state-metrics-0\",\"service\":\"tke-kube-state-metrics\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_scene_flag\":\"true\"},{\"__name__\":\"up\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"container\":\"node-exporter\",\"instance\":\"10.0.0.185\",\"job\":\"node-exporter\",\"namespace\":\"kube-system\",\"pod\":\"tke-node-exporter-rltlc\",\"service\":\"tke-node-exporter\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_scene_flag\":\"true\"},{\"__name__\":\"up\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"container\":\"node-exporter\",\"instance\":\"10.0.0.196\",\"job\":\"node-exporter\",\"namespace\":\"kube-system\",\"pod\":\"tke-node-exporter-4lcms\",\"service\":\"tke-node-exporter\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_scene_flag\":\"true\"},{\"__name__\":\"up\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"instance\":\"10.0.0.3:9091\",\"job\":\"job1\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_scene_flag\":\"true\"},{\"__name__\":\"up\",\"cluster\":\"cls-qzzzqko6\",\"cluster_type\":\"tke\",\"instance\":\"10.0.0.3:9091\",\"job\":\"job2\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\",\"tke_scene_flag\":\"true\"}]}"
        },
        "RequestId": "uv8-r34jqub--2zkzgtj3p26cwmjcjfw"
    }
}
```

**Example 5: 点查询(Instant query)**

```
Path: api/v1/query
Method: GET POST
Query参数: 
   1. query = <string> prometheus查询表达式
   2. time = <rfc3339 | unix_timestamp> 查询数据的时间
   3. timeout = <duration> 超时时间 (1m / 5s / ...)
响应体:
{
	"status": "success" | "error",
	"data": {
		"resultType": "matrix" | "vector" | "scalar" | "string",
		"result": <value>
	},
	
	// 错误时返回
	"errorType": "<string>",
	"error": "<string>",

	// warning 信息
	"warnings": ["<string>"]
}
```
查询结果result字段参考[prometheus点查询结果编码](https://prometheus.io/docs/prometheus/latest/querying/api/#expression-query-result-formats)

Input: 

```
tccli monitor RoutePrometheusDynamicAPI --cli-unfold-argument  \
    --InstanceId prom-xz223asd \
    --Method GET \
    --Path /api/v1/query?query=ALERTS{}&time=1700534157&timeout=30s
```

Output: 
```
{
    "Response": {
        "HTTP": {
            "StatusCode": 200,
            "ResponseBody": "{\"status\":\"success\",\"data\":{\"resultType\":\"vector\",\"result\":[{\"metric\":{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_language_\":\"zh-CN\",\"_policyname_\":\"alertgroup-in-tke/alert-2\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"4611686018429437801\",\"_uin_\":\"1500000688\",\"alertname\":\"alertgroup-in-tke/alert-2\",\"alertstate\":\"firing\",\"severity\":\"warning\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},\"value\":[1700534157,\"1\"]},{\"metric\":{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_interval_\":\"5m\",\"_language_\":\"zh-CN\",\"_policyid_\":\"arule-2wou7mfi\",\"_policyname_\":\"test-monitor-alert\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"100026263254\",\"_uin_\":\"1500000688\",\"alertname\":\"test-monitor-alert\",\"alertstate\":\"firing\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},\"value\":[1700534157,\"1\"]},{\"metric\":{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_language_\":\"zh-CN\",\"_policyname_\":\"al-test-changed/aaaaa\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"100026263254\",\"_uin_\":\"1500000688\",\"alertname\":\"al-test-changed/aaaaa\",\"alertstate\":\"firing\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},\"value\":[1700534157,\"1\"]},{\"metric\":{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_language_\":\"zh-CN\",\"_policyname_\":\"alertgroup-in-tke/alert-1\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"4611686018429437801\",\"_uin_\":\"1500000688\",\"alertname\":\"alertgroup-in-tke/alert-1\",\"alertstate\":\"firing\",\"severity\":\"warning\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},\"value\":[1700534157,\"1\"]}]}}"
        },
        "RequestId": "8-ztbsc3gc2-rw6lzn4gfg5kuz6khrxg"
    }
}
```

**Example 6: 范围查询(Range query)**

```
Path: /api/v1/query_range
Method: GET POST
Query参数: 
   1. query = <string> prometheus查询表达式
   2. start = <rfc3339 | unix_timestamp> 查询起始时间
   3. end = <rfc3339 | unix_timestamp> 查询结束时间 (结束时间要晚于起始时间)
   4. step = <duration | float> 查询步长 (1m / 15s / ... 或浮点数秒)
   5. timeout = <duration> 超时时间 (1m / 5s / ...)
响应体:
{
	"status": "success" | "error",
	"data": {
		"resultType": "matrix",
		"result": <value>
	},
	
	// 错误时返回
	"errorType": "<string>",
	"error": "<string>",

	// warning 信息
	"warnings": ["<string>"]
}
```
查询结果result字段参考[prometheus范围查询结果编码](https://prometheus.io/docs/prometheus/latest/querying/api/#range-vectors)

Input: 

```
tccli monitor RoutePrometheusDynamicAPI --cli-unfold-argument  \
    --InstanceId prom-xz223asd \
    --Method GET \
    --Path /api/v1/query_range?query=ALERTS{}&start=1700535380&end=1700535680&step=1m&timeout=20s
```

Output: 
```
{
    "Response": {
        "HTTP": {
            "StatusCode": 200,
            "ResponseBody": "{\"status\":\"success\",\"data\":{\"resultType\":\"matrix\",\"result\":[{\"metric\":{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_interval_\":\"5m\",\"_language_\":\"zh-CN\",\"_policyid_\":\"arule-2wou7mfi\",\"_policyname_\":\"test-monitor-alert\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"100026263254\",\"_uin_\":\"1500000688\",\"alertname\":\"test-monitor-alert\",\"alertstate\":\"firing\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},\"values\":[[1700535380,\"1\"],[1700535440,\"1\"],[1700535500,\"1\"],[1700535560,\"1\"],[1700535620,\"1\"],[1700535680,\"1\"]]},{\"metric\":{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_language_\":\"zh-CN\",\"_policyname_\":\"al-test-changed/aaaaa\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"100026263254\",\"_uin_\":\"1500000688\",\"alertname\":\"al-test-changed/aaaaa\",\"alertstate\":\"firing\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},\"values\":[[1700535380,\"1\"],[1700535440,\"1\"],[1700535500,\"1\"],[1700535560,\"1\"],[1700535620,\"1\"],[1700535680,\"1\"]]},{\"metric\":{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_language_\":\"zh-CN\",\"_policyname_\":\"alertgroup-in-tke/alert-1\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"4611686018429437801\",\"_uin_\":\"1500000688\",\"alertname\":\"alertgroup-in-tke/alert-1\",\"alertstate\":\"firing\",\"severity\":\"warning\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},\"values\":[[1700535380,\"1\"],[1700535440,\"1\"],[1700535500,\"1\"],[1700535560,\"1\"],[1700535620,\"1\"],[1700535680,\"1\"]]},{\"metric\":{\"__name__\":\"ALERTS\",\"_appid_\":\"1251763868\",\"_instanceid_\":\"prom-7031abs0\",\"_language_\":\"zh-CN\",\"_policyname_\":\"alertgroup-in-tke/alert-2\",\"_region_\":\"ap-chongqing\",\"_regionid_\":\"19\",\"_subaccountuin_\":\"4611686018429437801\",\"_uin_\":\"1500000688\",\"alertname\":\"alertgroup-in-tke/alert-2\",\"alertstate\":\"firing\",\"severity\":\"warning\",\"tcloud_region_id\":\"19\",\"tcloud_region_name\":\"ap-chongqing\"},\"values\":[[1700535380,\"1\"],[1700535440,\"1\"],[1700535500,\"1\"],[1700535560,\"1\"],[1700535620,\"1\"],[1700535680,\"1\"]]}]}}"
        },
        "RequestId": "ms6le5eg5-l16rh6fr2f6r57h3eiolbh"
    }
}
```


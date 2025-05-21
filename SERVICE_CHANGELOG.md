# Release 3.0.1205.1

## 腾讯云数据仓库 TCHouse-D(cdwdoris) 版本：2021-12-28

### 第 60 次发布

发布时间：2025-05-22 01:17:17

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ReduceInstance](http://document.tencentcloudapi.woa.com/document/product/1706/84347)

	* 新增入参：CheckAuth

* [ScaleOutInstance](http://document.tencentcloudapi.woa.com/document/product/1706/82855)

	* 新增入参：CheckAuth

* [ScaleUpInstance](http://document.tencentcloudapi.woa.com/document/product/1706/82854)

	* 新增入参：CheckAuth, RollingRestart




## 日志服务(cls) 版本：2020-10-16

### 第 115 次发布

发布时间：2025-05-22 01:20:51

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateDataTransform](http://document.tencentcloudapi.woa.com/document/product/614/72184)

	* 新增入参：ProcessFromTimestamp, ProcessToTimestamp

* [CreateScheduledSql](http://document.tencentcloudapi.woa.com/document/product/614/81265)

	* 新增入参：FullQuery

* [DescribeKafkaConsumer](http://document.tencentcloudapi.woa.com/document/product/614/81449)

	* 新增出参：EnableInternetConsume, EnableIntranetConsume

* [ModifyKafkaConsumer](http://document.tencentcloudapi.woa.com/document/product/614/81450)

	* 新增入参：EnableInternetConsume, EnableIntranetConsume

* [ModifyScheduledSql](http://document.tencentcloudapi.woa.com/document/product/614/81385)

	* 新增入参：FullQuery

* [OpenKafkaConsumer](http://document.tencentcloudapi.woa.com/document/product/614/72339)

	* 新增入参：EnableInternetConsume, EnableIntranetConsume


修改数据结构：

* [DataTransformTaskInfo](http://document.tencentcloudapi.woa.com/document/product/614/56471#DataTransformTaskInfo)

	* 新增成员：ProcessFromTimestamp, ProcessToTimestamp, HistoryTaskStatus

* [ScheduledSqlTaskInfo](http://document.tencentcloudapi.woa.com/document/product/614/56471#ScheduledSqlTaskInfo)

	* 新增成员：FullQuery




## 数据传输服务(dts) 版本：2021-12-06



## 数据传输服务(dts) 版本：2018-03-30

### 第 11 次发布

发布时间：2025-05-22 01:30:58

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [DstInfo](http://document.tencentcloudapi.woa.com/document/product/571/18131#DstInfo)




## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 92 次发布

发布时间：2025-05-22 01:33:13

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateGroupsSTD](http://document.tencentcloudapi.woa.com/document/product/589/86882)

新增数据结构：

* [GroupInfo](http://document.tencentcloudapi.woa.com/document/product/589/33981#GroupInfo)
* [ResultItem](http://document.tencentcloudapi.woa.com/document/product/589/33981#ResultItem)



## 数据加速器 GooseFS(goosefs) 版本：2022-05-19

### 第 16 次发布

发布时间：2025-05-22 01:37:51

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateFileset](http://document.tencentcloudapi.woa.com/document/product/1716/86888)
* [DeleteFileset](http://document.tencentcloudapi.woa.com/document/product/1716/86887)
* [DescribeFilesetGeneralConfig](http://document.tencentcloudapi.woa.com/document/product/1716/86886)
* [DescribeFilesets](http://document.tencentcloudapi.woa.com/document/product/1716/86885)
* [UpdateFileset](http://document.tencentcloudapi.woa.com/document/product/1716/86884)
* [UpdateFilesetGeneralConfig](http://document.tencentcloudapi.woa.com/document/product/1716/86883)

新增数据结构：

* [FilesetInfo](http://document.tencentcloudapi.woa.com/document/product/1716/81241#FilesetInfo)



## 物联网开发平台(iotexplorer) 版本：2019-04-23

### 第 75 次发布

发布时间：2025-05-22 01:43:28

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [VisionRecognitionResult](http://document.tencentcloudapi.woa.com/document/product/1081/34988#VisionRecognitionResult)

	* 新增成员：AlternativeSummary




## 云数据库 KeeWiDB(keewidb) 版本：2022-03-08

### 第 7 次发布

发布时间：2025-05-22 01:46:55

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeInstances](http://document.tencentcloudapi.woa.com/document/product/1712/80428)

	* 新增入参：TagList




## 轻量应用服务器(lighthouse) 版本：2020-03-24

### 第 72 次发布

发布时间：2025-05-22 01:47:33

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [Blueprint](http://document.tencentcloudapi.woa.com/document/product/1207/47576#Blueprint)

	* 新增成员：SupportScanLogin




## 消息队列 MQTT 版(mqtt) 版本：2024-05-16

### 第 13 次发布

发布时间：2025-05-22 01:53:50

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyInstance](http://document.tencentcloudapi.woa.com/document/product/1773/85729)

* [ModifyInstanceCertBinding](http://document.tencentcloudapi.woa.com/document/product/1773/85772)

	* <font color="#dd0000">**修改入参**：</font>SSLServerCertId, SSLCaCertId

* [ModifyJWTAuthenticator](http://document.tencentcloudapi.woa.com/document/product/1773/84954)

	* 新增入参：Status


修改数据结构：

* [MQTTMessageItem](http://document.tencentcloudapi.woa.com/document/product/1773/84898#MQTTMessageItem)

* [PublicAccessRule](http://document.tencentcloudapi.woa.com/document/product/1773/84898#PublicAccessRule)

	* <font color="#dd0000">**修改成员**：</font>IpRule, Allow




## 云数据库 PostgreSQL(postgres) 版本：2017-03-12

### 第 43 次发布

发布时间：2025-05-22 01:57:43

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**删除接口**：</font>

* UpgradeDBInstance



## SSL 证书(ssl) 版本：2019-12-05

### 第 81 次发布

发布时间：2025-05-22 02:02:50

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CertificateInfoSubmit](http://document.tencentcloudapi.woa.com/document/product/400/85744)

	* 新增入参：Type, CaType




## 腾讯云国际站(tencentcloudintl) 版本：2020-05-20

### 第 2 次发布

发布时间：2025-05-22 02:09:52

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeDocWriteList](http://document.tencentcloudapi.woa.com/document/product/1795/86890)
* [DescribeDocumentList](http://document.tencentcloudapi.woa.com/document/product/1795/86889)

新增数据结构：

* [DescribeDocWrite](http://document.tencentcloudapi.woa.com/document/product/1795/86675#DescribeDocWrite)
* [DescribeDocWriteList](http://document.tencentcloudapi.woa.com/document/product/1795/86675#DescribeDocWriteList)
* [DescribeDocumentList](http://document.tencentcloudapi.woa.com/document/product/1795/86675#DescribeDocumentList)
* [DocumentItem](http://document.tencentcloudapi.woa.com/document/product/1795/86675#DocumentItem)



## 实时音视频(trtc) 版本：2019-07-22

### 第 91 次发布

发布时间：2025-05-22 02:15:12

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ServerPushText](http://document.tencentcloudapi.woa.com/document/product/647/44055#ServerPushText)

	* 新增成员：DropMode, Priority




## 微服务引擎(tse) 版本：2020-12-07

### 第 90 次发布

发布时间：2025-05-22 02:15:55

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [GovernanceAlias](http://document.tencentcloudapi.woa.com/document/product/1364/54942#GovernanceAlias)

	* 新增成员：Metadatas

* [GovernanceNamespace](http://document.tencentcloudapi.woa.com/document/product/1364/54942#GovernanceNamespace)

	* 新增成员：Metadatas

* [GovernanceServiceContract](http://document.tencentcloudapi.woa.com/document/product/1364/54942#GovernanceServiceContract)

	* 新增成员：Metadatas

* [KVPair](http://document.tencentcloudapi.woa.com/document/product/1364/54942#KVPair)

	* <font color="#dd0000">**修改成员**：</font>Key, Value

* [SREInstance](http://document.tencentcloudapi.woa.com/document/product/1364/54942#SREInstance)

	* 新增成员：GlobalType, GroupType, GroupId, IsMainRegion





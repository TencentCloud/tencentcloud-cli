# Release 3.0.1340.1

## 大模型安全网关(apis) 版本：2024-08-01

### 第 2 次发布

发布时间：2026-01-05 01:09:49

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAgentApp](http://document.tencentcloudapi.woa.com/document/product/1805/87895)

	* 新增入参：OAuth2ResourceServerID

* [DescribeAgentApps](http://document.tencentcloudapi.woa.com/document/product/1805/87886)

* [DescribeMcpServers](http://document.tencentcloudapi.woa.com/document/product/1805/87901)

* [ModifyAgentApp](http://document.tencentcloudapi.woa.com/document/product/1805/87885)

	* 新增入参：OAuth2ResourceServerID


修改数据结构：

* [AgentAppMcpServerDTO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#AgentAppMcpServerDTO)

	* 新增成员：SSEResourceIdentifier, StreamableResourceIdentifier

* [AgentAppMcpServerVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#AgentAppMcpServerVO)

	* 新增成员：SSEResourceIdentifier, StreamableResourceIdentifier

* [DescribeAgentAppResp](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeAgentAppResp)

	* 新增成员：OAuth2ResourceServerID, McpServersNum




## 云数据库 MySQL(cdb) 版本：2017-03-20

### 第 155 次发布

发布时间：2026-01-05 01:15:55

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeDBInstanceConfig](http://document.tencentcloudapi.woa.com/document/product/236/17491)

	* 新增入参：NeedRsInfo

	* 新增出参：MasterIp, MasterPort




## 云防火墙(cfw) 版本：2019-09-04

### 第 85 次发布

发布时间：2026-01-05 01:19:28

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeCcnVpcFwPolicyLimit](http://document.tencentcloudapi.woa.com/document/product/1132/88620)
* [DescribeClusterVpcFwSwitchs](http://document.tencentcloudapi.woa.com/document/product/1132/88621)

新增数据结构：

* [AttachInsInfo](http://document.tencentcloudapi.woa.com/document/product/1132/49071#AttachInsInfo)
* [ClusterSwitchDetail](http://document.tencentcloudapi.woa.com/document/product/1132/49071#ClusterSwitchDetail)
* [EndpointInfo](http://document.tencentcloudapi.woa.com/document/product/1132/49071#EndpointInfo)



## 云安全一体化平台(csip) 版本：2022-11-21

### 第 62 次发布

发布时间：2026-01-05 01:24:10

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [AccessKeyAlarmCount](http://document.tencentcloudapi.woa.com/document/product/1726/80814#AccessKeyAlarmCount)

	* 新增成员：AccessKeyStatus, AccessKeyCreateTime, LastAccessTime

* [AccessKeyRisk](http://document.tencentcloudapi.woa.com/document/product/1726/80814#AccessKeyRisk)

	* 新增成员：CloudType, RelatedAK




## 数据库智能管家 DBbrain(dbbrain) 版本：2021-05-27

### 第 49 次发布

发布时间：2026-01-05 01:30:52

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeRedisUnExpiredKeyStatistics](http://document.tencentcloudapi.woa.com/document/product/1130/88622)

修改接口：

* [DescribeRedisTopBigKeys](http://document.tencentcloudapi.woa.com/document/product/1130/72832)

	* 新增入参：UnExpireKey

	* <font color="#dd0000">**修改入参**：</font>Date


新增数据结构：

* [RedisGlobalKeyInfo](http://document.tencentcloudapi.woa.com/document/product/1130/57812#RedisGlobalKeyInfo)



## 数据库智能管家 DBbrain(dbbrain) 版本：2019-10-16



## 消息队列 TDMQ(tdmq) 版本：2020-02-17

### 第 168 次发布

发布时间：2026-01-05 02:08:22

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeRocketMQGeneralSKUs](http://document.tencentcloudapi.woa.com/document/product/1179/88623)

新增数据结构：

* [GeneralSKU](http://document.tencentcloudapi.woa.com/document/product/1179/46089#GeneralSKU)
* [PriceTag](http://document.tencentcloudapi.woa.com/document/product/1179/46089#PriceTag)



## 容器服务(tke) 版本：2022-05-01



## 容器服务(tke) 版本：2018-05-25

### 第 108 次发布

发布时间：2026-01-05 02:12:10

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [SuperNodeResource](http://document.tencentcloudapi.woa.com/document/product/457/31866#SuperNodeResource)

	* 新增成员：PriceType




## 实时音视频(trtc) 版本：2019-07-22

### 第 115 次发布

发布时间：2026-01-05 02:15:12

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [StartAIConversation](http://document.tencentcloudapi.woa.com/document/product/647/84215)

	* 新增入参：SignalConfig


修改数据结构：

* [AudioFormat](http://document.tencentcloudapi.woa.com/document/product/647/44055#AudioFormat)

	* 新增成员：Bitrate





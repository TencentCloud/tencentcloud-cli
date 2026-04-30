# Release 3.0.1415.1

## 数据开发治理平台 WeData(wedata) 版本：2025-10-10

### 第 19 次发布

发布时间：2026-05-01 02:34:43

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [GetNotebookPreloadScript](http://document.tencentcloudapi.woa.com/document/product/1607/89448)

	* 新增入参：MLEnabled

* [UpdateMLModelService](http://document.tencentcloudapi.woa.com/document/product/1607/89832)

	* 新增入参：CronScaleJobs, ModelHotUpdateEnable, MaxRetryTimes, RollingUpdate, SchedulingStrategy, HorizontalPodAutoscaler, ScaleStrategy, ServiceEIPInfo


新增数据结构：

* [CronScaleJob](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CronScaleJob)
* [HorizontalPodAutoscaler](http://document.tencentcloudapi.woa.com/document/product/1607/88970#HorizontalPodAutoscaler)
* [NumOrPercent](http://document.tencentcloudapi.woa.com/document/product/1607/88970#NumOrPercent)
* [RollingUpdate](http://document.tencentcloudapi.woa.com/document/product/1607/88970#RollingUpdate)

修改数据结构：

* [CreateServiceInfos](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CreateServiceInfos)

	* 新增成员：InstancePerReplicas, ScaleStrategy, ServiceEIPInfo, CronScaleJobs, ModelHotUpdateEnable, SchedulingStrategy, RollingUpdate, HorizontalPodAutoscaler

* [MLModelService](http://document.tencentcloudapi.woa.com/document/product/1607/88970#MLModelService)

	* 新增成员：HorizontalPodAutoscaler, InstancePerReplicas, ScaleStrategy, TerminationGracePeriodSeconds, CronScaleJobs, ModelHotUpdateEnable, MaxRetryTimes, RollingUpdate, SchedulingStrategy

* [ServiceEIPInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ServiceEIPInfo)

	* <font color="#dd0000">**修改成员**：</font>ServiceId, VpcId, SubnetId




## 数据开发治理平台 WeData(wedata) 版本：2025-08-06



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20




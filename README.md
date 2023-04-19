# Serverless Sample SAM with Datadog.

This is a simple voting service built on a Serverless Architecture using AWS SAM. It features [Datadog's Serverless monitoring](https://docs.datadoghq.com/serverless/). The backend consists of Lambda, API Gateway, SQS, and DynamoDB, all used in conjunction. It's built with a combination of Python and Node, making it a multi-language application. All major features of Datadog Lambda monitoring are enabled.

## Architecture

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbwPYVu%2FbtsacgylnCk%2F6sYxokqPW2RpQxVDmzWzqK%2Fimg.png" style="width:100%; height:100%"/>

## Pages

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FptnsN%2Fbtr93lHBVfy%2FKTcWZHlSpkkvLm8QKURAfK%2Fimg.png" style="width:35%; height:35%"/>

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdfKxYj%2Fbtr91yt61S5%2Fx0HsnMNH9oU7o1I15IXPL1%2Fimg.png" style="width:35%; height:35%"/>

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FnndhH%2FbtsaceHi5z3%2FkWzBc82NU7Fl1R1v1vc6EK%2Fimg.png" style="width:35%; height:35%"/>

## URL

[https://datadoghq.net](https://datadoghq.net)
[https://datadoghq.net/en](https://datadoghq.net/en)

## Create a SAM

```sh
## In order to use AWS SAM, it needs to be installed first. (https://docs.aws.amazon.com/ko_kr/serverless-application-model/latest/developerguide/serverless-getting-started.html)
# git clone
git clone https://github.com/leedoing/DatadogServerlessSampleSAM.git

# Create SAM Datadog stack
aws cloudformation create-stack \
  --stack-name datadog-serverless-macro \
  --template-url https://datadog-cloudformation-template.s3.amazonaws.com/aws/serverless-macro/latest.yml \
  --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM

# Deploy SAM
sam deploy --guided


---
```

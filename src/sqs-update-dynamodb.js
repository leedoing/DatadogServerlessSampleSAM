const AWS = require("aws-sdk");
const ddb = new AWS.DynamoDB.DocumentClient();
const { DDB_VOTES_TABLE_NAME } = process.env;

const UpdateDynamoDB = async function (body) {
  try {
    for (const key in body.vote_name) {
      await ddb
        .update({
          TableName: DDB_VOTES_TABLE_NAME,
          Key: {
            vote_name: body.vote_name[key],
          },
          UpdateExpression: `SET votes = if_not_exists(votes, :default_votes) + :value`,
          ExpressionAttributeValues: {
            ":default_votes": 0,
            ":value": 1,
          },
        })
        .promise();
      console.log("Update DynamoDB Success");
    }
    return {};
  } catch (err) {
    console.error("Update DynamoDB Error: ", err);
    return {};
  }
};

exports.handler = async (event) => {
  let win = "";
  console.log(JSON.stringify(event));
  // Process SQS messages in batch, up to 10 records in each batch
  for (const record of event.Records) {
    const messageId = record.messageId;
    console.log("MessageId: ", messageId);

    // SQS record body includes entire API POST request
    const recordBody = JSON.parse(record.body);
    console.log("SqsRecordBody: ", JSON.stringify(recordBody));

    // Example body from API POST request: {"id":"dog"}
    const requestBody = JSON.parse(recordBody.body);
    const data = await UpdateDynamoDB(requestBody);
  }

  return {
    statusCode: 200,
    headers: {
      "Access-Control-Allow-Headers": "Content-Type",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "OPTIONS,POST",
      "Timing-Allow-Origin": "*",
    },
    body: "Update DynamoDB Success",
  };
};

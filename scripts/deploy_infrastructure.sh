#!/bin/bash
set -e

STACK_PREFIX="churn-segmentation"

echo "Deploying artifacts stack..."
aws cloudformation deploy --stack-name ${STACK_PREFIX}-artifacts --template-file ../infrastructure/cloudformation/artifacts.yaml --capabilities CAPABILITY_NAMED_IAM

echo "Deploying IAM stack..."
aws cloudformation deploy --stack-name ${STACK_PREFIX}-iam --template-file ../infrastructure/cloudformation/iam.yaml --capabilities CAPABILITY_NAMED_IAM

echo "Deploying CodeBuild stack..."
aws cloudformation deploy --stack-name ${STACK_PREFIX}-codebuild --template-file ../infrastructure/cicd/codebuild.yaml --capabilities CAPABILITY_NAMED_IAM

echo "Deploying CodePipeline stack..."
aws cloudformation deploy --stack-name ${STACK_PREFIX}-codepipeline --template-file ../infrastructure/cicd/codepipeline.yaml --capabilities CAPABILITY_NAMED_IAM

echo "All stacks deployed successfully."
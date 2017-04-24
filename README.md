## How to set up a load balanced and redundant Flask WebApp on ECS with Docker 

### 1 Configure the ECS cluster

Sign in to AWS. You will need a verified account.

##### 1.1 Create ECS cluster

Navigate to the EC2 Container Services (ECS) service. Create a new cluster. Tick the "Create an empty cluster" checkbox and click 'Create'. Thats it for now.

##### 1.2 Setup load balancer

From the 'Services' menu, choose the EC2 console. Scroll down on the left hand menu and select 'Load Balancers'. Create a new load balancer - we chose the 'Classic Load Balancer' for no particular reason. 

In Step 1 of the wizard, we chose a name and went with the default options. In Step 2, we configured a new security group which allowed traffic on port 80. We are going to ignore the need for a Secure Listener (SSL terminator) in step 3. In step 4, configure the ping path to '/', as that's all docker can handle. Skip adding EC2 instances for now. Skip adding tags and review and create your load balancer. 

##### 1.3 Configure roles for EC2, ECS and ELB communication

Before creating an auto-scaling group, you will need a couple of appropriate IAM roles to be created.

Firstly, by default your EC2 instances do not have permissions to talk to an ECS cluster, you need to create a role to support this. This role will be attached to your EC2 instances when we create them. From the IAM services console, choose an 'Amazon EC2' AWS Service Role. You will need to attach the 'AmazonEC2ContainerServiceforEC2Role' policy for your new role.

Secondly, you need a role to allow the ECS cluster to talk to your ELB. From the 'AWS Service Roles' select 'Amazon EC2 Container Service Role' and attach the 'AmazonEC2ContainerServiceRole' policy to your role.

##### 1.4 Setup an auto-scaling group

From the EC2 console, scroll down to 'Auto Scaling Groups'. Create an auto-scaling group and create a launch configuration. Choose an AMI from the AWS Marketplace - 'Amazon ECS-Optimised Amazon Linux AMI'. We chose General Purpose t2.micro. Set the name of your launch configuration and assign the IAM role you created for allowing your EC2 instances to talk to your ECS cluster.

From Advanced Details drop down menu, add the following bash script to the User Data section:

```
#!/bin/bash

echo ECS_CLUSTER=flask-test-ecs-cluster > /etc/ecs/ecs.config
```

Next, accept the default EBS volume for storage and proceed to creating a security group. Create a new security group with a HTTP rule which allows traffic from anywhere. Create the launch configuration and proceed without a keypair as the instance will only need to host a docker image.

Now, create your auto scaling group with the default VPC and any of the default subnets.

For now, keep the auto scaling group at its initial size, ignore notifications and tags.


### 2 Create and Dockerise WebApp 

(tbc)

### 3 Publish Webapp to ECS cluster

(tbc)






### Deploying a Flask application in AWS: An end-to-end tutorial

This is the code that goes along with the detailed writeup here:

https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80

It's a simple Flask app that writes and reads from a database. It uses Amazon RDS for the database backend, but you can make things even simpler and use a local DB.

To tool around with the app directly, here's a quickstart guide. 

Clone this repo to your local machine. In the top level directory, create a virtual environment:
```
$ virtualenv flask-aws
$ source flask-aws/bin/activate
```
Now install the required modules:
```
$ pip install -r requirements.txt
```
To play with the app right away, you can use a local database. Edit ```config.py``` by commenting out the AWS URL and uncomment this line:
```
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
```
Next run:
```
$ python db_create.py
```
And the tables are created.  Now you can launch the app:
```
$ python application.py
```
And point your browser to http://0.0.0.0:5000

Using the top form, you can write to the database:

![Site main page](http://i.imgur.com/2d66GIB.png)

![Data entered](http://i.imgur.com/AQWdD2Q.png)

Get confirmation:

![confirmaton](http://i.imgur.com/JtemL7a.png)

Using the bottom form, you can see the last 1 to 9 entires of the database in reverse chronological order:

![results](http://i.imgur.com/LFJeKDz.png)



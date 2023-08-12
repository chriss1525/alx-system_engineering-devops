#0x18-webstack_monitoring

## Table of Contents
[Prerequisites](#Prerequisites)


[Getting Datadog API Key](#Getting-Datadog-API-Key)


[Installing Datadog Agent on Ubuntu](#Installing-Datadog-Agent-on-Ubuntu)


[Creating a Monitoring Dashboard](#Creating-a-Monitoring-Dashboard)


[Tracking Read and Write Metrics](#Tracking-Read-and-Write-Metrics)


## Prerequisites
- Datadog account (Sign up at Datadog)
- Ubuntu machine

## Getting Datadog API Key
- Log in to your Datadog account.
- In the Datadog application, navigate to Integrations > APIs.
- Generate a new API key.
- Copy the API key for future use.


## Installing Datadog Agent on Ubuntu
- SSH into your Ubuntu machine.

- Run the following commands to install the Datadog Agent:

```bash
Copy code
DD_API_KEY=YOUR_API_KEY_HERE
bash -c "$(curl -L https://raw.githubusercontent.com/DataDog/datadog-agent/master/cmd/agent/install_script.sh)"
```


- Wait for the installation to complete.


## Tracking Read and Write Metrics
To track read and write metrics per minute using the Datadog web interface and create separate monitors for them, follow these steps:

- Log in to your Datadog account.
- In the Datadog application, navigate to Monitors > New Monitor.
- Choose the Metric option to start configuring your metric-based monitor.

### Creating Monitor for Read Operations:
In the "Create Monitor" page for the read operations monitor:

- Set the metric to system.io.r_s to monitor read operations per second.
- Configure other parameters such as the time range and aggregation as needed.
- Define alert conditions for read operations:
   - {{#is_alert}}Reads per second alert testif{{/is_alert}}
- Choose notification channels to receive alerts (e.g., email, Slack, PagerDuty).
- Give your monitor a meaningful name and description to identify its purpose (e.g., "Read Operations Monitor").

- Save the monitor.

### Creating Monitor for Write Operations:
Create another monitor following the same steps for the write operations:

- Set the metric to system.io.w_s to monitor write operations per second.
- Configure parameters, alert conditions, and notification channels accordingly.
- Define alert conditions for write operations:
   -  {{#is_alert}}Writes per second alert testif{{/is_alert}}
- Give this monitor a name and description (e.g., "Write Operations Monitor").

- Save the monitor.

## Creating a Monitoring Dashboard
- Log in to your Datadog account.
- In the Datadog application, navigate to Dashboards > New Dashboard.
- Add widgets to the dashboard to visualize metrics:
   - Click on New Widget.
   - Choose the metric you want to display (e.g., CPU usage, memory usage).
   - Customize the widget's appearance and settings.
- Repeat for other relevant metrics.

## Conclusion
Congratulations! You've successfully set up Datadog, installed the agent on Ubuntu, created a monitoring dashboard, and started tracking read and write metrics. Feel free to customize and expand your monitoring setup as needed.

For more information, refer to the Datadog Documentation.

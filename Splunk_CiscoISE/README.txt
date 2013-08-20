Copyright (C) 2005-2013 Splunk Inc. All Rights Reserved.

Add-on:            Splunk for Cisco Firewalls (PIX, FWSM, ASA)
Current Version:   2.0.1
Last Modified:     2013-01-29
Splunk Version:    4.3 and higher
Author:            Splunk, Inc.

The Splunk for Cisco Firewalls add-on allows you to consume, analyze, and report on Cisco firewall data for Cisco ASA, PIX and FWSM firewalls. This add-on is designed to work with the Splunk Cisco Security Suite; install these together to access reports and dashboards that give you visual insight into your Cisco Firewall data.

##### What's New #####
2.0 (2012-04-01)
- Major updaate to the app.
- Completely change the look and feel of the app.
- Refactor the code base.

1.0.1 (2011-05-22)
- Resolved minor issue (SOLN-1639) within the Cisco Firewall dashboards that causes a “ValueError(22,”Invalid Argument”) error when running Cisco Firewall on a Windows system.

1.0.0 (2011-03-08)
- Add-on officially supported by Splunk, Inc.
- Updated to provide compatibility with Splunk 4.2
- Added a new setup to provide automated configuration of the TCP and UDP syslog inputs

##### Technology Add-on Details ######

Sourcetype(s):            cisco_firewall
Supported Technologies:   Cisco ASA, FWSM and PIX firewall devices
Compatible Solutions:     Cisco Security Suite

###### Installation Instructions ######

The Cisco Firewalls add-on can be downloaded, installed, and configured to receive Cisco firewall data by either using the Splunk app setup screen or by manually installing and configuring the add-on.  Instructions for both methods are described.

+++ Automated setup using the add-on setup +++

The automated setup is designed to walk you through the configuration of the Cisco Firewalls add-on once the add-on is installed on your Splunk deployment.  The setup screen can be accessed in one of the following ways:

1. Click the "Setup" button on the add-on from within the Splunk Home page.
2. Click the Welcome > Add data > Cisco device logs > Get other apps and add-ons for Cisco devices - Visit Splunkbase
3. Click Manager > Apps > Cisco Firewalls > "Set up" 

The setup program will configure a port on the Splunk server to listen for UDP or TCP traffic from your firewall devices.  Once the desired configuration options are selected, click the "Save" button.  The setup program will create and/or update the inputs.conf file to include the desired input configuration.

Note: You are also given the option to disable previous versions of Cisco Firewalls.  If any changes exist in local they will need to be manually migrated over to this new add-on.

You can reopen the setup screen at any time by navigating to  Manager > Apps > Cisco Firewalls > "Set up".

+++ Manual setup and configuration +++

1. Open the inputs.conf file (or create a new one if it does not already exist) located at $SPLUNK_HOME/etc/apps/cisco_firewall/local/inputs.conf

2. Modify the inputs.conf file to include the following stanza for each network port listening on firewall data.

For example:

   [udp://514]
   disabled = false

Do not specify a sourcetype.  The add-on will automatically assign sourcetypes for your ASA, FWSM and PIX firewall events as cisco_pix, cisco_asa and cisco_fwsm, accordingly.

3. Save the changes made to the inputs.conf file.

Splunk requires a restart before the scripted input will take effect.  

Note: This add-on has been renamed from previous versions (namely "_addon" has been removed).  Optionally you may choose to manually remove the "cisco_firewall_addon" add-on from the file system.  If any changes exist in local they will need to be manually migrated over to this add-on.

###### Troubleshooting the add-on ######

If you have previously indexed Cisco firewall data and would like to preserve the current sourcetype for reporting purposes you can create an alias in the local directory of this app.

To create a sourcetype alias simply add the following entry to props.conf under the local directory of this app ($SPLUNK_HOME/etc/apps/cisco_firewall_addon/local):

[cisco_firewall]
rename = your_current_firewall_sourcetype


The field extractions are set to sourcetype=cisco_firewall which is keyed off of %ASA, %PIX and %FWSM. All of the reports use eventtype=cisco_firewall, the default cisco_firewall eventtype looks for %ASA, %PIX or %FWSM in your data.

The real time and overview dashboards as well as the included searches and reports in this add-on rely on the search: eventtype=cisco_firewall in order to report on firewall data. 


###### Using summary indexing with the Cisco Firewalls add-on ######


+++ Enabling summary indexing for this add-on +++

There is one scheduled search included in this add-on which creates a summary stash every 6 hours with a Splunk enterprise license.
To change the schedule you can edit the following search under the manager:

Cisco Firewall - DataCube - Summary Index

To enable summary index reporting on your dashboard create the following stanza in cisco_firewall_addon/local/macros.conf

[cisco_firewall]
definition = index=summary marker=cisco_firewall 


+++ Changing the default schedule +++

There is one scheduled search included in this add-on which creates a cache for the dashboard every 3 hours with a Splunk enterprise license.

To change the schedule you can edit the following search under the manager:

Cisco Firewall - DataCube

###### Getting Help ######

* Additional information regarding the installation and configuration of the Cisco Firewalls add-on can be found here:
http://splunk-base.splunk.com/answers/3366/how-do-i-install-the-cisco-firewall-add-on

* See Splunk Answers to view existing questions and answers regarding the Cisco Firewalls add-on or to ask a question yourself:
http://splunk-base.splunk.com/search/?q=cisco+firewall&Submit=search

* Alternatively, contact Splunk technical support: support@splunk.com

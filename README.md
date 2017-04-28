# Exlink #
Control your Samsung TV using a serial port.
This is a fork from [Miguel Hernandez Martos]' original [Exlink].
## Exlink Protocol ##
Samsung provides a serial port on many older 'smart TVs', i.e. the ones that are smart enough to 'do stuff' but not smart enough to be controlled using the modern Web/SOAP (network) interfaces.  The location and wiring for these serials ports is described the [SamyGO wiki] but beware of the most important issue:
> Samsung TV Serial ports are wired for TTL (3.3V) voltages.  Connecting them directly to a real 12V serial port will kill them!
## Components and Tools ##
Exlink contains the following components and tools:
  * **exlink**, the main class that talks to the Samsung TV via the serial port; includes methods such as 'volumeUp()'
  * **exlinkCodes**, definitions a many of the available functions that can be requested from the Samsung TV; support for individual codes varies by TV model
  * **json_exlink**, a simple web server that accepts JSON requests and converts them to TV control requests
  * **samsung_tv**, an example application that demonstrates using exlink to control a Samsung TV.

### Dependencies ###
The following lists the Python packages on which Exlink depends:
 * exlink
   * pySerial
 * json_exlink
   * aniso8601==1.0.0
   * Flask==0.10.1
   * Flask-RESTful==0.3.3
   * itsdangerous==0.24
   * Jinja2==2.7.3
   * MarkupSafe==0.23
   * pyserial==2.7
   * pytz==2015.4
   * six==1.9.0
   * Werkzeug==0.10.4

### Development
Paul (papadeltasierra) is happy to receive suggestions.

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Miguel Hernandez Martos]:  <https://github.com/enlavin>
   [Exlink]: <https://github.com/enlavin/exlink>
   [SamyGO wiki]: <http://wiki.samygo.tv/index.php?title=Main_Page#ES_series_Ex-Link_cable_and_Service_Port_connection>
 
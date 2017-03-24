# ruckus2dokuwiki
This python script pulls the runs the "sh tech support" command on a Ruckus ZoneDirector and dumps the output into a dokuwiki page for backup and reference


### Recommendations ###

I'd recommend using a subnamespace for your config files in dokuwiki so that your ZoneDirector config is not mixed in with the rest of your dokuwiki pages and your file operations are limited to a single directory.  Example:  If you have a namespace "IT" in dokuwiki create a subname space named "IT:ruckus" so that your config files are in their own directory.  You'd then have a directory named /path-to-dokuwiki/data/pages/it/ruckus/ and in order to reference the config in dokuwiki you'd use [[IT:ruckus:zonedirector | ZoneDirector]]

### Usage ###

  1. Clone this script to your server running both dokuwiki
  2. Make sure to modify your paths so that they read from the proper directory and write to the proper directory
  3. Run the script and verify that everything works (I run this script at root)
  4. Create a cron entry to run the script occassionally (Hourly if you make lots of changes, daily if you make infrequent changes)
  
### NOTES: ###

I'm new to python so I'm sure this code could be WAY better but it does what I need it to.  I'll optimize it eventually. 

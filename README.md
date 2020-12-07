## RvCrunch- RVTools reporter

RvCrunch is a simple CLI tool that provides a report with relevant information for a Veeam sizing. The base function produces a report with an environment breakdown.

There are also mini reports that provide quick reports on key information from the RvTools report.

The tool accepts RvTools files in excel format (.xlsx)

The script requries 'pandas' and 'numpy' to be installed within the Python environment for the script to run.

`pip install pandas numpy`

Specifying the file path as the first arguement will run the main "Crunch" report. Using the optional parameter -sr or --skipreport will skip this report.

Example:
`python .\rvcrunch.py "C:\path\to\rvtools\rvtools.xlsx`

Using -po or --poweredon will only display Powered On virtual machine info, otherwise both Powered Off machines will also be listed.

Using -sn or --savename allows you to specify the report name, otherwise the default 'report.xlsx' will be used.

Using -vse or --vseexport will export a VSE compatible txt file that can be uploaded.
Note that the will be Powered On VMs only and the main report must be run.

There are also several mini reports that provide certain key info, these are shown in the command line.
-vm : Provides the total VM count
-dc : Provides the Datacenter names
-cl : Provides the Cluster names
-dc_cl : Groups the clusters by the Datacenter
-rdm : Export an excel with RDMs by VM plus capacity in TB (optional export)

These can be run alongside the main report or instead. To prevent the main report being run when using mini reports use the -sr flag.

Example:
`python .\rvcrunch.py -sr -vm "C:\path\to\rvtools\rvtools.xlsx`

Note: RDM report is allocated capacity, mapping the disks in vDisk to the paritions in vPartition isn't precises enough to be practical.

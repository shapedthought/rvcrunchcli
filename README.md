# RvCrunch- RVTools reporter

RvCrunch is a simple CLI tool that provides a report with relevant information from a RvTools export. The main function is to save an Excel report with this information.

The report includes a 'Agg Cap' figure which uses the vPartitions tab to calculate a more accurate used capacity figure. Where VMs are missing because they are powered off or VMware tools is not working, the allocated capacity will be shown in that column.

RvCrunch relies on the excellent work done by Rob de Veij of [RvTools](https://www.robware.net/rvtools/) fame.

There are also mini reports that provide quick reports on key information from the RvTools report.

The tool accepts RvTools files in excel format (.xlsx), vInfo and vParition tabs are required.

## Installation

You can install RvCrunch from PyPi via:

`pip install rvcrunch`

## Usage

Run the tool via the commandline via:

`rvcrunch [OPTIONS] path`

Specifying the file path as the first arguement will run the main Excel "Crunch" report.

`rvcrunch "C:\path\to\rvtools\rvtools.xlsx"`

-po or --poweredon modifies the report to display only Powered On virtual machine info.

-sn or --savename allows you to specify the exported file name, otherwise the default 'report.xlsx' will be used.

-sr or --skipreport stops the main report being exported to excel, this can be used with the mini reports below.

There are also several mini reports that provide certain key info, these are shown in the command line.

-vm : Provides the total VM count by Powered-On and Off

-dc : Provides the Datacenter names

-cl : Provides the Cluster names

-dc_cl : Groups the clusters by the Datacenter and provides vm, disk and vInfo capacity breakdowns.

-rdm : Checks if report has RDMs and optionally exports to Excel. The vDisk tab is required for this to work.

These can be run alongside the main report or instead. To prevent the main report being run when using mini reports use the -sr flag.

Example:
`rvcrunch -sr -vm "C:\path\to\rvtools\rvtools.xlsx"`

Note: RDM report is allocated capacity, mapping the disks in vDisk to the paritions in vPartition isn't precise enough to be practical.

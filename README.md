Neuroanalysis forked repository
=============

This is a fork of the original Neuroanalysis repository, which can be found at https://github.com/AllenInstitute/neuroanalysis. The original repository is maintained by the Allen Institute and contains tools for analysis of neurophysiology data, with emphasis on patch-clamp electrophysiology.

This fork is a copy of commit 59bd8de (SHA 59bd8dee4ea6bf71695153125210e29ac9f33cb1) that ensures compatibility with aisynphys database and the associated raw data formats. The original repository may have undergone changes since that commit, so this fork may not include the latest updates or features from the original repository.

The following changes to the original repository have been implemented in this fork:
- remove pyqtgraph dependency







Neuroanalysis
=============

Modular and interactive tools for analysis of neurophysiology data, with emphasis on 
patch-clamp electrophysiology.

* Functions for running common analysis algorithms
    * Synaptic/calcium event detection and characterization
    * Synaptic release modeling
    * VC and CC spike detection and characterization
    * VC and CC test pulse analysis
    * Basic signal processing (filtering, baseline removal, etc.)
* Data abstraction layer to allow adapting new data formats (see neuroanalysis/data.py)
* Re-usable user interface elements for implementing common analysis tasks


Status
------

This project is early in development and does not yet have a stable API.
Issues and pull requests are accepted (see CONTRIBUTING.md), but may not be 
reviewed or accepted on any fixed schedule.






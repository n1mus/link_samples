/*
A KBase module: link_samples
*/

module link_samples {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_link_samples(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};

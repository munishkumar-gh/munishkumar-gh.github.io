/*(function () {
    var myConnector = tableau.makeConnector();

    myConnector.getSchema = function (schemaCallback) {

    };

    myConnector.getData = function (table, doneCallback) {

    };

    tableau.registerConnector(myConnector);
})();

$(document).ready(function () {
    $("#submitButton").click(function () {
        tableau.connectionName = "<Title as defined in html document>";
        tableau.submit();
    });
});*/


(function () {
    var myConnector = tableau.makeConnector();

    myConnector.getSchema = function (schemaCallback) {
        var cols = [{
            id: "Month",
            dataType: tableau.dataTypeEnum.date
        }, {
            id: "total_rainfall",
            alias: "Monthly Total Rainfall",
            dataType: tableau.dataTypeEnum.float
        }];

        var tableSchema = {
            id: "rainfall_monthly_total",
            alias: "The total monthly rainfall recorded at the Changi Climate Station",
            columns: cols
        };

        schemaCallback([tableSchema]);
    };
    
    myConnector.getData = function(table, doneCallback) {
    $.getJSON("https://data.gov.sg/dataset/rainfall-monthly-total/resource/778814b8-1b96-404b-9ac9-68d6c00e637b/view/be92ce92-d02e-4920-9479-ff6da87b45e8", function(resp) {
            var feat = resp.features,
                tableData = [];

            // Iterate over the JSON object
            for (var i = 0, len = feat.length; i < len; i++) {
                tableData.push({
                    "Month": feat[i].id,
                    //"Monthly Total Rainfall": feat[i].properties.mag,
                    "Monthly Total Rainfall": feat[i].properties.total_rainfall,
                    //"location": feat[i].geometry
                });
            }

            table.appendRows(tableData);
            doneCallback();
        });
    };

    tableau.registerConnector(myConnector);
})();

$(document).ready(function () {
    $("#submitButton").click(function () {
        tableau.connectionName = "Government Data Feed - Open Source";
        tableau.submit();
    });
});




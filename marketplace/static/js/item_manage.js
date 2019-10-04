var dataset = [
    [
        "1",
        "alexander",
        "alexander@test.com",
        "xxxxxxxxx",
        "600",
        "24/04/2015"
    ],
    [
        "2",
        "HenryVII",
        "mrmoneybags@test.com",
        "xxxxxxxxx",
        "755",
        "25/04/2015"
    ],
    [
        "3",
        "Roosevelt1858",
        "teddybear@test.com",
        "xxxxxxxxx",
        "800",
        "26/04/2015"
    ],
    [
        "4",
        "JuliusCaesar",
        "idontlikesharpthings@test.com",
        "xxxxxxxxx",
        "950",
        "25/04/2015"
    ],
    [
        "5",
        "alexander",
        "alexander@test.com",
        "xxxxxxxxx",
        "1000",
        "25/04/2015"
    ],
    [
        "6",
        "HenryVIII",
        "kingofengland@test.com",
        "xxxxxxxxx",
        "1200",
        "26/04/2015"
    ]
]


$(document).ready(function () {
    var table =$('#bidtable').DataTable({
        data: dataset,
        columns: [
            { title: "ID" },
            { title: "Username" },
            { title: "Bidder-Email" },
            { title: "Phone" },
            { title: "Bid-Amount" },
            { title: "Bid-Time" },
            { title: "Details" } 
        ],
        "columnDefs": [ {
            "targets": -1,
            "data": null,
            "defaultContent": "<button class='btn btn-orange' data-toggle='modal' data-target='#modelSelectBid'>Select</button>"
        } ]
    });
    $('#bidtable tbody').on( 'click', 'button', function () {
        var data = table.row( $(this).parents('tr') ).data();
        $(".modal-body").html("<p>Do you want to sell this item for <b>$" + data[4] +"</b> to the user <b>" + data[1] + "</b>?</p>");
        
    });
});
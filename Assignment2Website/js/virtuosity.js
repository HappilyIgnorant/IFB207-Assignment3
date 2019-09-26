$(window).scroll(function () {
    if ($(this).scrollTop() > 0)
    {
        $('.hidenav').fadeOut();
    } else
    {
        $('.hidenav').fadeIn();
    }
});

from booking.booking import Booking

    
with Booking() as bot:
    
    bot.land_first_page()
    bot.change_currency()
    bot.select_destination("Zadar")
    bot.select_dates_box()
    bot.select_dates('2025-04-13', '2025-04-17')
    bot.select_persons(2)
    bot.search_button()
    bot.apply_filters()
    #bot.refresh() in case the printed results dont match the results on the webpage
    bot.report_results()
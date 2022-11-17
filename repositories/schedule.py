import datetime
from .query_helpers import QueryHelpers as Query

class ScheduleRepository:
    """
    Data access layer for scheduling
    """

    @staticmethod
    def get_current_show():
        """
        Gets the current show as a dict object.
        """

        sql = """
            select 
                id,
                title,
                info,
                show_image,
                strftime(start_date_time) as start_date_time,
                strftime(end_date_time) as end_date_time
            from schedule_show
            where start_date_time < %s
            and end_date_time > %s
            and active = 1
        """

        now = datetime.datetime.now()

        return Query.single(sql , [now, now])


    @staticmethod
    def get_shows(startDate, endDate):
        """
        Returns all active shows that have been scheduled between a provided date range.
        """

        sql = """
            select 
                id,
                title,
                info,
                show_image,
                strftime(start_date_time) as start_date_time,
                strftime(end_date_time) as end_date_time
            from schedule_show
            where active = 1
            and date between %s and %s
            order by date, start_time
        """

        return Query.many(sql, [startDate, endDate])
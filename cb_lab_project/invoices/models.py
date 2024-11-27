from django.db import models

class DetailLine(models.Model):
    guest_check_line_item_id = models.AutoField(primary_key=True)
    guest_check = models.ForeignKey('GuestCheck', on_delete=models.CASCADE)
    rvc_num = models.IntegerField(null=True, blank=True)
    dtl_ot_num = models.IntegerField(null=True, blank=True)
    dtl_oc_num = models.IntegerField(null=True, blank=True)
    line_num = models.IntegerField()
    dtl_id = models.IntegerField(null=True, blank=True)
    detail_utc = models.DateTimeField(null=True, blank=True)
    detail_lcl = models.DateTimeField(null=True, blank=True)
    last_update_utc = models.DateTimeField(null=True, blank=True)
    last_update_lcl = models.DateTimeField(null=True, blank=True)
    bus_dt = models.DateField(null=True, blank=True)
    ws_num = models.IntegerField(null=True, blank=True)
    dsp_ttl = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    dsp_qty = models.IntegerField(null=True, blank=True)
    agg_ttl = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    agg_qty = models.IntegerField(null=True, blank=True)
    chk_emp_id = models.IntegerField(null=True, blank=True)
    chk_emp_num = models.IntegerField(null=True, blank=True)
    svc_rnd_num = models.IntegerField(null=True, blank=True)
    seat_num = models.IntegerField(null=True, blank=True)
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE)

    class Meta:
        db_table = 'detail_lines'

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    cur_utc = models.DateTimeField(auto_now_add=True)
    loc_ref = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'restaurant'


class GuestCheck(models.Model):
    guest_check_id = models.AutoField(primary_key=True)
    chk_num = models.IntegerField()
    opn_bus_dt = models.DateField(auto_now_add=True)
    opn_utc = models.DateTimeField(auto_now_add=True)
    opn_lcl = models.DateTimeField(auto_now_add=True)
    clsd_bus_dt = models.DateField(auto_now=True)
    clsd_utc = models.DateTimeField(null=True, blank=True)
    clsd_lcl = models.DateTimeField(null=True, blank=True)
    last_trans_utc = models.DateTimeField(null=True, blank=True)
    last_trans_lcl = models.DateTimeField(null=True, blank=True)
    last_updated_utc = models.DateTimeField(null=True, blank=True)
    last_updated_lcl = models.DateTimeField(null=True, blank=True)
    clsd_flag = models.BooleanField(default=False)
    gst_cnt = models.IntegerField()
    sub_ttl = models.DecimalField(max_digits=12, decimal_places=2)
    non_txbl_sls_ttl = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    chk_ttl = models.DecimalField(max_digits=12, decimal_places=2)
    dsc_ttl = models.DecimalField(max_digits=12, decimal_places=2)
    pay_ttl = models.DecimalField(max_digits=12, decimal_places=2)
    bal_due_ttl = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    rvc_num = models.IntegerField()
    ot_num = models.IntegerField()
    oc_num = models.IntegerField(null=True, blank=True)
    tbl_num = models.IntegerField()
    tbl_name = models.CharField(max_length=255)
    emp_num = models.IntegerField()
    num_srvc_rd = models.IntegerField()
    num_chk_prntd = models.IntegerField()
    restaurant_id = models.IntegerField()

    class Meta:
        db_table = 'guest_checks'


class TaxType(models.Model):
    tax_type_id = models.AutoField(primary_key=True)
    tax_type_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    type = models.IntegerField()

    class Meta:
        db_table = 'tax_types'


class Tax(models.Model):
    tax_num = models.AutoField(primary_key=True)
    guest_check = models.ForeignKey('GuestCheck', on_delete=models.CASCADE)
    tax_type = models.ForeignKey('TaxType', on_delete=models.CASCADE)
    txbl_sls_ttl = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    tax_coll_ttl = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'taxes'

class MenuItem(models.Model):
    menu_item_id = models.AutoField(primary_key=True)
    mod_flag = models.BooleanField(default=False)
    incl_tax = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    active_taxes = models.CharField(max_length=255, null=True, blank=True)
    prc_lvl = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'menu_items'

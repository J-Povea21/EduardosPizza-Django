davur_folder_name="davur"
frontend_folder_name="frontend"
general_folder_name="general"


dz_array = {
    "davur":{
        "davur_views":{
        "public":{
            "favicon":f"{general_folder_name}/images/favicon.png",
            "title":"Eduardo's Pizza",
            "social_image_url":"https://davur.dexignzone.com/django/social-image.png"
        },
        "global":{
            "css":[
                    f"{davur_folder_name}/vendor/bootstrap-select/dist/css/bootstrap-select.min.css",
                    f"{davur_folder_name}/css/style.css"
                ],
            "js":{
                "top":[
                    f"{davur_folder_name}/vendor/global/global.min.js",
                    f"{davur_folder_name}/vendor/bootstrap-select/dist/js/bootstrap-select.min.js"
                ],
                "bottom":[
                    f"{davur_folder_name}/js/custom.js",
                    f"{davur_folder_name}/js/deznav-init.js",
                ]
            },

        },
        "pagelevel":{
            "css": {
                "index":[
                    f"{davur_folder_name}/vendor/jqvmap/css/jqvmap.min.css",
                    f"{davur_folder_name}/vendor/chartist/css/chartist.min.css"
                ],  
                "page_analytics":[
                    f"{davur_folder_name}/vendor/jqvmap/css/jqvmap.min.css",
                    f"{davur_folder_name}/vendor/chartist/css/chartist.min.css"
                ],
                "page_review":[
                    f"{davur_folder_name}/vendor/jqvmap/css/jqvmap.min.css",
                    f"{davur_folder_name}/vendor/chartist/css/chartist.min.css",
                    f"{davur_folder_name}/vendor/owl-carousel/owl.carousel.css"
                ],
                "page_order":[
                    f"{davur_folder_name}/vendor/jqvmap/css/jqvmap.min.css",
                    f"{davur_folder_name}/vendor/chartist/css/chartist.min.css"

                ],
                "page_order_list":[
                    f"{davur_folder_name}/vendor/datatables/css/jquery.dataTables.min.css"
                ],
                "page_general_customers":[
                    f"{davur_folder_name}/vendor/datatables/css/jquery.dataTables.min.css"
                ],






                "permissions":[
                    f"{davur_folder_name}/vendor/sweetalert2/dist/sweetalert2.min.css", 
                ],

                "users":[
                    f"{davur_folder_name}/vendor/sweetalert2/dist/sweetalert2.min.css",    
                ],
                "add_user":[
                    f"{davur_folder_name}/vendor/bootstrap-daterangepicker/daterangepicker.css",
                    f"{davur_folder_name}/vendor/select2/css/select2.min.css",
                ],
                "edit_user":[
                    f"{davur_folder_name}/vendor/bootstrap-daterangepicker/daterangepicker.css",
                    f"{davur_folder_name}/vendor/select2/css/select2.min.css",
                ],
                "groups_list":[
                    f"{davur_folder_name}/vendor/sweetalert2/dist/sweetalert2.min.css",
                ],
                "assign_permissions_to_user":[

                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/prettify.min.css",
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/src/bootstrap-duallistbox.css",
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/dist/bootstrap-duallistbox.css",
                ],

                "group_add":[
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/prettify.min.css",
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/src/bootstrap-duallistbox.css",
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/dist/bootstrap-duallistbox.css",
                ],


                "group_edit":[
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/prettify.min.css",
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/src/bootstrap-duallistbox.css",
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/dist/bootstrap-duallistbox.css",
                ],








                "app_profile":[
                    f"{davur_folder_name}/vendor/lightgallery/css/lightgallery.min.css",
                    f"{davur_folder_name}/vendor/magnific-popup/magnific-popup.css"
                ],
                "post_details":[
                    f"{davur_folder_name}/vendor/lightgallery/css/lightgallery.min.css",
                    f"{davur_folder_name}/vendor/magnific-popup/magnific-popup.css"
                ],
                "email_compose":[
                    f"{davur_folder_name}/vendor/dropzone/dist/dropzone.css"
                ],
                "email_inbox":[],
                "email_read":[],
                "app_calender":[
                    f"{davur_folder_name}/vendor/fullcalendar/css/main.min.css"
                ],
                "ecom_product_grid":[],
                "ecom_product_list":[],
                "ecom_product_detail":[
                    f"{davur_folder_name}/vendor/owl-carousel/owl.carousel.css"
                ],
                "ecom_product_order":[],
                "ecom_checkout":[],
                "ecom_invoice":[],
                "ecom_customers":[],

                "chart_float":[],
                "chart_morris":[],
                "chart_chartjs":[],
                "chart_chartist":[
                    f"{davur_folder_name}/vendor/chartist/css/chartist.min.css"
                ],
                "chart_sparkline":[],
                "chart_peity":[],

                "ui_accordion":[],
                "ui_alert":[],
                "ui_badge":[],
                "ui_button":[],
                "ui_modal":[],
                "ui_button_group":[],
                "ui_list_group":[],
                "ui_media_object":[],
                "ui_card":[],
                "ui_carousel":[],
                "ui_dropdown":[],
                "ui_popover":[],
                "ui_progressbar":[],
                "ui_tab":[],
                "ui_typography":[],
                "ui_pagination":[],
                "ui_grid":[],
                "uc_select2":[
                    f"{davur_folder_name}/vendor/select2/css/select2.min.css"
                ],
                "uc_nestable":[
                    f"{davur_folder_name}/vendor/nestable2/css/jquery.nestable.min.css"
                ],
                "uc_noui_slider":[
                    f"{davur_folder_name}/vendor/nouislider/nouislider.min.css"
                ],
                "uc_sweetalert":[
                    f"{davur_folder_name}/vendor/sweetalert2/dist/sweetalert2.min.css"
                ],
                "uc_toastr":[
                    f"{davur_folder_name}/vendor/toastr/css/toastr.min.css"
                ],
                "map_jqvmap":[
                    f"{davur_folder_name}/vendor/jqvmap/css/jqvmap.min.css"
                ],
                "uc_lightgallery":[
                    f"{davur_folder_name}/vendor/lightgallery/css/lightgallery.min.css"
                ],
                "widget_basic":[
                    f"{davur_folder_name}/vendor/chartist/css/chartist.min.css"
                ],
                "form_element":[],
                "form_wizard":[
                    f"{davur_folder_name}/vendor/jquery-steps/css/jquery.steps.css",
                    f"{davur_folder_name}/vendor/jquery-smartwizard/dist/css/smart_wizard.min.css",
                ],
                "form_ckeditor":[],
                "form_pickers":[
                    f"{davur_folder_name}/vendor/bootstrap-daterangepicker/daterangepicker.css",
                    f"{davur_folder_name}/vendor/clockpicker/css/bootstrap-clockpicker.min.css",
                    f"{davur_folder_name}/vendor/jquery-asColorPicker/css/asColorPicker.min.css",
                    f"{davur_folder_name}/vendor/bootstrap-material-datetimepicker/css/bootstrap-material-datetimepicker.css",
                    f"{davur_folder_name}/vendor/pickadate/themes/default.css",
                    f"{davur_folder_name}/vendor/pickadate/themes/default.date.css",
                ],
                "form_validation_jquery":[],
                "table_bootstrap_basic":[],
                "table_datatable_basic":[
                    f"{davur_folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                ],
                "page_error_400":[],
                "page_error_403":[],
                "page_error_404":[],
                "page_error_500":[],
                "page_error_503":[],
                "page_register":[],
                "page_login":[],
                "page_lock_screen":[],
                "page_forgot_password":[],
            },
            ##********************************************************

            # Javascript

            #**********************************************************
            "js":{
                "index":[
                    f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                    f"{davur_folder_name}/js/deznav-init.js",
                    f"{davur_folder_name}/vendor/waypoints/jquery.waypoints.min.js",
                    f"{davur_folder_name}/vendor/jquery.counterup/jquery.counterup.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                    f"{davur_folder_name}/vendor/peity/jquery.peity.min.js",
                    f"{davur_folder_name}/js/dashboard/dashboard-1.js"
                ],
                "page_analytics":[
                    f"{davur_folder_name}/vendor/waypoints/jquery.waypoints.min.js",
                    f"{davur_folder_name}/vendor/jquery.counterup/jquery.counterup.min.js",
                    f"{davur_folder_name}/vendor/peity/jquery.peity.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                    f"{davur_folder_name}/js/dashboard/analytics.js"
                ],
                "page_review":[
                    f"{davur_folder_name}/vendor/owl-carousel/owl.carousel.js"
                ],
                "page_order":[
                    f"{davur_folder_name}/vendor/waypoints/jquery.waypoints.min.js",
                    f"{davur_folder_name}/vendor/jquery.counterup/jquery.counterup.min.js",
                    f"{davur_folder_name}/vendor/peity/jquery.peity.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js"

                ],
                "page_order_list":[
                    f"{davur_folder_name}/vendor/datatables/js/jquery.dataTables.min.js"
                ],
                "page_general_customers":[
                    f"{davur_folder_name}/vendor/datatables/js/jquery.dataTables.min.js"
                ],






                "permissions":[
                    f"{davur_folder_name}/vendor/sweetalert2/dist/sweetalert2.min.js",
                ],

                "users":[
                    f"{davur_folder_name}/vendor/sweetalert2/dist/sweetalert2.min.js",

                ],
                "add_user":[
                    f"{davur_folder_name}/vendor/moment/moment.min.js",
                    f"{davur_folder_name}/vendor/bootstrap-daterangepicker/daterangepicker.js",
                    f"{davur_folder_name}/vendor/select2/js/select2.full.min.js",
                    f"{davur_folder_name}/js/plugins-init/select2-init.js"
                ],
                "edit_user":[
                    f"{davur_folder_name}/vendor/moment/moment.min.js",
                    f"{davur_folder_name}/vendor/bootstrap-daterangepicker/daterangepicker.js",
                    f"{davur_folder_name}/vendor/select2/js/select2.full.min.js",
                    f"{davur_folder_name}/js/plugins-init/select2-init.js"
                ],
                "groups_list":[
                    f"{davur_folder_name}/vendor/sweetalert2/dist/sweetalert2.min.js",
                ],
                "assign_permissions_to_user":[
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/popper.js/1.12.9/umd/popper.min.js",
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/run_prettify.js",
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/dist/jquery.bootstrap-duallistbox.js",
                ],
                "group_add":[
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/popper.js/1.12.9/umd/popper.min.js",
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/run_prettify.js",
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/dist/jquery.bootstrap-duallistbox.js",
                ],

                "group_edit":[
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/popper.js/1.12.9/umd/popper.min.js",
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/run_prettify.js",
                    f"{davur_folder_name}/vendor/bootstrap-duallistbox/dist/jquery.bootstrap-duallistbox.js",
                ],














                "app_profile":[
                    f"{davur_folder_name}/vendor/lightgallery/js/lightgallery-all.min.js",
                    f"{davur_folder_name}/vendor/magnific-popup/jquery.magnific-popup.js"

                ],
                "post_details":[
                    f"{davur_folder_name}/vendor/lightgallery/js/lightgallery-all.min.js",
                    f"{davur_folder_name}/vendor/magnific-popup/jquery.magnific-popup.js"

                ],
                "email_compose":[
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                    f"{davur_folder_name}/vendor/dropzone/dist/dropzone.js"
                ],
                "email_inbox":[
                    f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js"
                ],
                "email_read":[
                    f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js"
                ],
                "app_calender":[
                    f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                    f"{davur_folder_name}/vendor/jqueryui/js/jquery-ui.min.js",
                    f"{davur_folder_name}/vendor/moment/moment.min.js",
                    f"{davur_folder_name}/vendor/fullcalendar/js/main.min.js",
                    f"{davur_folder_name}/js/plugins-init/fullcalendar-init.js",
                ],
                "ecom_product_grid":[
                    f"{davur_folder_name}/vendor/highlightjs/highlight.pack.min.js",
                
                ],
                "ecom_product_list":[
                    f"{davur_folder_name}/vendor/highlightjs/highlight.pack.min.js",
                    f"{davur_folder_name}/vendor/star-rating/jquery.star-rating-svg.js", 
                ],
                "ecom_product_detail":[
                    f"{davur_folder_name}/vendor/owl-carousel/owl.carousel.js",
                    f"{davur_folder_name}/vendor/highlightjs/highlight.pack.min.js",
                    f"{davur_folder_name}/vendor/star-rating/jquery.star-rating-svg.js",
                ],
                "ecom_product_order":[
                    f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                    f"{davur_folder_name}/vendor/highlightjs/highlight.pack.min.js",
                ],
                "ecom_checkout":[
                    f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                    f"{davur_folder_name}/vendor/highlightjs/highlight.pack.min.js"
                ],
                "ecom_invoice":[
                    f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                    f"{davur_folder_name}/vendor/highlightjs/highlight.pack.min.js",
                    
                ],
                "ecom_customers":[
                    f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                    f"{davur_folder_name}/vendor/highlightjs/highlight.pack.min.js",
                ],
                "chart_flot":[
                    f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                    f"{davur_folder_name}/vendor/flot/jquery.flot.js",
                    f"{davur_folder_name}/vendor/flot/jquery.flot.pie.js",
                    f"{davur_folder_name}/vendor/flot/jquery.flot.resize.js",
                    f"{davur_folder_name}/vendor/flot-spline/jquery.flot.spline.min.js",
                    f"{davur_folder_name}/js/plugins-init/flot-init.js"
                ],
                "chart_morris":[
                    f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                    f"{davur_folder_name}/vendor/raphael/raphael.min.js",
                    f"{davur_folder_name}/vendor/morris/morris.min.js",
                    f"{davur_folder_name}/js/plugins-init/morris-init.js",
                ],
                "chart_chartjs":[
                    f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                    f"{davur_folder_name}/js/plugins-init/chartjs-init.js",  
                ],
                "chart_chartist":[
                    f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                    f"{davur_folder_name}/vendor/chartist/js/chartist.min.js",
                    f"{davur_folder_name}/vendor/chartist-plugin-tooltips/js/chartist-plugin-tooltip.min.js",
                    f"{davur_folder_name}/js/plugins-init/chartist-init.js",
                ],
                "chart_sparkline":[
                    f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                    f"{davur_folder_name}/vendor/jquery-sparkline/jquery.sparkline.min.js",
                    f"{davur_folder_name}/js/plugins-init/sparkline-init.js",
                    f"{davur_folder_name}/vendor/svganimation/vivus.min.js",
                    f"{davur_folder_name}/vendor/svganimation/svg.animation.js"
                ],
                "chart_peity":[
                    f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                    f"{davur_folder_name}/vendor/peity/jquery.peity.min.js",
                    f"{davur_folder_name}/js/plugins-init/piety-init.js",
                ],

                "ui_accordion":[],
                "ui_alert":[],
                "ui_badge":[],
                "ui_button":[],
                "ui_modal":[],
                "ui_button_group":[],
                "ui_list_group":[],
                "ui_media_object":[],
                "ui_card":[],
                "ui_carousel":[],
                "ui_dropdown":[],
                "ui_popover":[],
                "ui_progressbar":[],
                "ui_tab":[],
                "ui_typography":[],
                "ui_pagination":[],
                "ui_grid":[],
                "uc_select2":[
                    f"{davur_folder_name}/vendor/select2/js/select2.full.min.js",
                    f"{davur_folder_name}/js/plugins-init/select2-init.js"

                ],
                "uc_nestable":[
                    f"{davur_folder_name}/vendor/nestable2/js/jquery.nestable.min.js",
                    f"{davur_folder_name}/js/plugins-init/nestable-init.js"
                ],
                "uc_noui_slider":[
                    f"{davur_folder_name}/vendor/nouislider/nouislider.min.js",
                    f"{davur_folder_name}/vendor/wnumb/wNumb.js",
                    f"{davur_folder_name}/js/plugins-init/nouislider-init.js",
                ],
                "uc_sweetalert":[
                    f"{davur_folder_name}/vendor/sweetalert2/dist/sweetalert2.min.js",
                    f"{davur_folder_name}/js/plugins-init/sweetalert.init.js"
                ],
                "uc_toastr":[
                    f"{davur_folder_name}/vendor/toastr/js/toastr.min.js",
                    f"{davur_folder_name}/js/plugins-init/toastr-init.js"
                ],
                "map_jqvmap":[
                    f"{davur_folder_name}/vendor/jqvmap/js/jquery.vmap.min.js",
                    f"{davur_folder_name}/vendor/jqvmap/js/jquery.vmap.world.js",
                    f"{davur_folder_name}/vendor/jqvmap/js/jquery.vmap.usa.js",
                    f"{davur_folder_name}/js/plugins-init/jqvmap-init.js",
                ],
                "uc_lightgallery":[
                    f"{davur_folder_name}/vendor/lightgallery/js/lightgallery-all.min.js"
                ],
                "widget_basic":[
                    f"{davur_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                    f"{davur_folder_name}/vendor/apexchart/apexchart.js",
                    f"{davur_folder_name}/vendor/chartist/js/chartist.min.js",
                    f"{davur_folder_name}/vendor/chartist-plugin-tooltips/js/chartist-plugin-tooltip.min.js",
                    f"{davur_folder_name}/vendor/flot/jquery.flot.js",
                    f"{davur_folder_name}/vendor/flot/jquery.flot.pie.js",
                    f"{davur_folder_name}/vendor/flot/jquery.flot.resize.js",
                    f"{davur_folder_name}/vendor/flot-spline/jquery.flot.spline.min.js",
                    f"{davur_folder_name}/vendor/jquery-sparkline/jquery.sparkline.min.js",
                    f"{davur_folder_name}/js/plugins-init/sparkline-init.js",
                    f"{davur_folder_name}/vendor/peity/jquery.peity.min.js",
                    f"{davur_folder_name}/js/plugins-init/piety-init.js",
                    f"{davur_folder_name}/js/plugins-init/widgets-script-init.js",
                ],
                "form_element":[],
                "form_wizard":[
                    f"{davur_folder_name}/vendor/jquery-steps/build/jquery.steps.min.js",
                    f"{davur_folder_name}/vendor/jquery-validation/jquery.validate.min.js",
                    f"{davur_folder_name}/js/plugins-init/jquery.validate-init.js",
                    f"{davur_folder_name}/vendor/jquery-smartwizard/dist/js/jquery.smartWizard.js",
                ],
                "form_ckeditor":[
                    f"{davur_folder_name}/vendor/ckeditor/ckeditor.js",
                ],
                "form_pickers":[
                    f"{davur_folder_name}/vendor/moment/moment.min.js",
                    f"{davur_folder_name}/vendor/bootstrap-daterangepicker/daterangepicker.js",
                    f"{davur_folder_name}/vendor/clockpicker/js/bootstrap-clockpicker.min.js",
                    f"{davur_folder_name}/vendor/jquery-asColor/jquery-asColor.min.js",
                    f"{davur_folder_name}/vendor/jquery-asGradient/jquery-asGradient.min.js",
                    f"{davur_folder_name}/vendor/jquery-asColorPicker/js/jquery-asColorPicker.min.js",
                    f"{davur_folder_name}/vendor/bootstrap-material-datetimepicker/js/bootstrap-material-datetimepicker.js",
                    f"{davur_folder_name}/vendor/pickadate/picker.js",
                    f"{davur_folder_name}/vendor/pickadate/picker.time.js",
                    f"{davur_folder_name}/vendor/pickadate/picker.date.js",
                    f"{davur_folder_name}/js/plugins-init/bs-daterange-picker-init.js",
                    f"{davur_folder_name}/js/plugins-init/clock-picker-init.js",
                    f"{davur_folder_name}/js/plugins-init/jquery-asColorPicker.init.js",
                    f"{davur_folder_name}/js/plugins-init/material-date-picker-init.js",
                    f"{davur_folder_name}/js/plugins-init/pickadate-init.js",
                ],
                "form_validation_jquery":[
                    f"{davur_folder_name}/vendor/jquery-validation/jquery.validate.min.js",
                    f"{davur_folder_name}/js/plugins-init/jquery.validate-init.js"
                ],
                "table_bootstrap_basic":[],
                "table_datatable_basic":[
                    f"{davur_folder_name}/vendor/datatables/js/jquery.dataTables.min.js",
                    f"{davur_folder_name}/js/plugins-init/datatables.init.js"
                ],
                "page_error_400":[],
                "page_error_403":[],
                "page_error_404":[],
                "page_error_500":[],
                "page_error_503":[],
                "page_register":[],
                "page_login":[],
                "page_lock_screen":[],
                "page_forgot_password":[],
                
            }

            }

    }#davur end
},
    "frontend":{
        "frontend_views":{
            "public":{
                "favicon":f"{general_folder_name}/images/favicon.png",
                "title":"Eduardo's Pizza",
                "social_image_url":"https://davur.dexignzone.com/django/social-image.png"
            },
            "global":{
                "css":[
                        f"{frontend_folder_name}/vendor/bootstrap-select/dist/css/bootstrap-select.min.css",
                        f"{frontend_folder_name}/css/style.css"
                    ],
                "js":{
                    "top":[
                        f"{frontend_folder_name}/vendor/global/global.min.js",
                        f"{frontend_folder_name}/vendor/bootstrap-select/dist/js/bootstrap-select.min.js"
                    ],
                    "bottom":[
                        f"{frontend_folder_name}/js/custom.js",
                        f"{frontend_folder_name}/js/deznav-init.js",
                    ]
                },

            },
            "pagelevel":{
                "css":{
                    "front_home":[
                        f"{frontend_folder_name}/vendor/owl-carousel/owl.carousel.css",
                        f"{frontend_folder_name}/vendor/bootstrap-touchspin/css/jquery.bootstrap-touchspin.min.css",
                        f"{frontend_folder_name}/vendor/swiper/css/swiper-bundle.css",
                    ],
                    "front_dashboard":[
                        f"{frontend_folder_name}/vendor/owl-carousel/owl.carousel.css",
                        f"{frontend_folder_name}/vendor/bootstrap-touchspin/css/jquery.bootstrap-touchspin.min.css",
                    ],
                    "front_authentication":[],
                    "front_booking":[
                        f"{frontend_folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "front_food_items":[
                        f"{frontend_folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "front_people":[
                        f"{frontend_folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "front_orders_status":[
                         f"{frontend_folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "front_reviews":[
                         f"{frontend_folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "front_setting":[
                        f"{frontend_folder_name}/vendor/jquery-asColorPicker/css/asColorPicker.min.css",
                        f"{frontend_folder_name}/vendor/bootstrap-select/dist/css/bootstrap-select.min.css",
                        f"{frontend_folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                        f"{frontend_folder_name}/css/all-min.css"

                    ],
                    "front_support":[],
                    "front_terms_conditions":[],
                    "front_transactions":[
                        f"{frontend_folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "front_upload_item":[
                         f"{frontend_folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "front_wallet":[
                        f"{frontend_folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "front_login":[],
                    "page_register":[],
                },
                "js":{
                    "front_home":[
                        f"{frontend_folder_name}/vendor/waypoints/jquery.waypoints.min.js",
                        f"{frontend_folder_name}/vendor/jquery.counterup/jquery.counterup.min.js",
                        f"{frontend_folder_name}/vendor/owl-carousel/owl.carousel.js",
                        f"{frontend_folder_name}/vendor/bootstrap-touchspin/js/jquery.bootstrap-touchspin.min.js",
                    ],
                    "front_dashboard":[
                        f"{frontend_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                        f"{frontend_folder_name}/vendor/waypoints/jquery.waypoints.min.js",
                        f"{frontend_folder_name}/vendor/jquery.counterup/jquery.counterup.min.js",
                        f"{frontend_folder_name}/vendor/apexchart/apexchart.js",
                        f"{frontend_folder_name}/vendor/owl-carousel/owl.carousel.js",
                        f"{frontend_folder_name}/vendor/bootstrap-touchspin/js/jquery.bootstrap-touchspin.min.js",
                        f"{frontend_folder_name}/js/dashboard/dashboard.js",

                    ],
                    "front_authentication":[],
                    "front_booking":[
                        f"{frontend_folder_name}/vendor/datatables/js/jquery.dataTables.min.js",
                    ],
                    "front_food_items":[
                        f"{frontend_folder_name}/vendor/datatables/js/jquery.dataTables.min.js",
                    ],
                    "front_people":[
                        f"{frontend_folder_name}/vendor/datatables/js/jquery.dataTables.min.js",
                    ],
                    "front_orders_status":[
                        f"{frontend_folder_name}/vendor/imagesloaded/imagesloaded.js",
                        f"{frontend_folder_name}/vendor/masonry/masonry-4.2.2.js",
                    ],
                    "front_reviews":[
                        f"{frontend_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                        f"{frontend_folder_name}/vendor/datatables/js/jquery.dataTables.min.js",
                    ],
                    "front_setting":[
                        f"{frontend_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                        f"{frontend_folder_name}/vendor/jquery-asColor/jquery-asColor.min.js",
                        f"{frontend_folder_name}/vendor/jquery-asGradient/jquery-asGradient.min.js",
                        f"{frontend_folder_name}/vendor/jquery-asColorPicker/js/jquery-asColorPicker.min.js",
                        f"{frontend_folder_name}/js/plugins-init/jquery-asColorPicker.init.js",
                    ],
                    "front_support":[],
                    "front_terms_conditions":[],
                    "front_transactions":[
                        f"{frontend_folder_name}/vendor/datatables/js/jquery.dataTables.min.js",
                    ],
                    "front_upload_item":[
                        f"{frontend_folder_name}/vendor/waypoints/jquery.waypoints.min.js",
                        f"{frontend_folder_name}/vendor/jquery.counterup/jquery.counterup.min.js",
                        f"{frontend_folder_name}/vendor/datatables/js/jquery.dataTables.min.js",
                    ],
                    "front_wallet":[
                        f"{frontend_folder_name}/vendor/chart.js/Chart.bundle.min.js",
                        f"{frontend_folder_name}/vendor/waypoints/jquery.waypoints.min.js",
                        f"{frontend_folder_name}/vendor/jquery.counterup/jquery.counterup.min.js",
                        f"{frontend_folder_name}/vendor/datatables/js/jquery.dataTables.min.js",
                    ],
                    "front_login":[],
                    "page_register":[],
                }
            }

        }
    }
}



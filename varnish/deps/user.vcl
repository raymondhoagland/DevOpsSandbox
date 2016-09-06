vcl 4.0;

backend default {
    .host = "haproxy";
    .port = "80";
}

sub vcl_recv
{
    if (req.url ~ "^/count")
    {
        return (pass);
    }
}
